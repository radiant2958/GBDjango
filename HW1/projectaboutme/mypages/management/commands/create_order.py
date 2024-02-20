from django.core.management.base import BaseCommand
from mypages.models import Order, Client, Product  
import random


class Command(BaseCommand):
    help = 'Creates a new order'

    def handle(self, *args, **options):
        # Select a random customer
        customer = Client.objects.order_by('?').first()

        # Select a random sample of products
        products = list(Product.objects.order_by('?')[:random.randint(1, Product.objects.count())])

        total_price = sum(product.price for product in products)

        # Create the order
        order = Order.objects.create(customer=customer, total_price=total_price)

        # Add products to the order
        for product in products:
            order.products.add(product)
        
        order.save()

        self.stdout.write(f'{order}')
