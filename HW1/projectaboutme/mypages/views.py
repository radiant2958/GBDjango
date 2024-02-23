from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Client, Order, Product
from .forms import UpdateProductForm, ProductForm

def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client).order_by('-date_ordered')

    return render(request, 'mypages/client_all_ordeers.html', {'client': client, 'orders': orders})

def client_orders_period(request, client_id, period):
    client = get_object_or_404(Client, pk=client_id)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=period)

    orders = Order.objects.filter(customer=client, date_ordered__gte=start_date).order_by('-date_ordered')

    products_info = {}

    for order in orders:
        for product in order.products.all():
            if product.id not in products_info:
                products_info[product.id] = {'product': product, 'date_ordered': order.date_ordered}

    products_with_dates = list(products_info.values())

    return render(request, 'mypages/client_orders_unique.html', {
        'client': client,
        'products_with_dates': products_with_dates,
        'period': period
    })

def changed_product(request):
    return render(request, 'mypages/changed_product.html')

def edit_product(request):
    product_id = request.GET.get('product_select')
    product_instance = None

    if product_id:
        product_instance = Product.objects.get(id=product_id)

    if request.method == "POST":
        form = UpdateProductForm(request.POST, instance=product_instance)
        if form.is_valid():
            form.save()
            return redirect('changed_product')  
    else:
        form = UpdateProductForm(instance=product_instance)

    return render(request, 'mypages/edit_product.html', {'form': form})

def success_url(request):
    return render(request, 'mypages/success_url.html') 

def product_creat_form(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = ProductForm()
    return render(request, 'mypages/product_creat_form.html', {'form': form})
