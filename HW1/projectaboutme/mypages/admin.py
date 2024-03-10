from asyncio import format_helpers
from django.contrib import admin
from .models import Client, Product, Order
from django.utils.html import format_html


@admin.register(Client)
class ModelClient(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'date_registered']
    list_filter = ['phone']
    list_display_links = ['name']
    fieldsets = (('Имя клиента', {'fields': ['name']}),
                 ('контактная информация', {'fields': ['email', 'phone', 'address']}))
    



@admin.register(Product)
class ModelProduct(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'date_add_product']
    list_filter = ['name']
    list_display_links = ['name']
    readonly_fields = ['image_preview',] 

    def image_preview(self, obj):
        return format_html('<img src="{}" width="300" height="auto" />', obj.image.url) if obj.image else "No image uploaded."
    image_preview.short_description = "Image Preview"


@admin.register(Order)
class ModelOrder(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone', 'total_price', 'date_ordered')
    readonly_fields = ('customer_info', 'products_list', 'total_price', 'date_ordered')
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_info',)
        }),
        ('Order Details', {
            'fields': ('products_list', 'total_price', 'date_ordered')
        }),
    )
    def customer_name(self, obj):
        return obj.customer.name
    customer_name.short_description = 'Customer Name'
    
    def customer_phone(self, obj):
        return obj.customer.phone
    customer_phone.short_description = 'Customer Phone'


    def customer_info(self, obj):
        return format_html(
            "<div><strong>Name:</strong> {}<br>"
            "<strong>Email:</strong> {}<br>"
            "<strong>Phone:</strong> {}<br>"
            "<strong>Address:</strong> {}<br>"
            "<strong>Registered:</strong> {}</div>",
            obj.customer.name, obj.customer.email, obj.customer.phone, 
            obj.customer.address, obj.customer.date_registered.strftime('%Y-%m-%d %H:%M')
        )
    customer_info.short_description = 'Customer Information'
    
    def products_list(self, obj):
        products = obj.products.all()
        product_details = "<div>"
        for product in products:
            product_details += f"<strong>ID:</strong> {product.id}, <strong>Name:</strong> {product.name}, <strong>Price:</strong> ${product.price}<br>"
        product_details += "</div>"
        return format_html(product_details)
    products_list.short_description = 'Products in Order'
   