from django.core.management.base import BaseCommand
from mypages.models import Order

class Command(BaseCommand):
    help = 'all orders'

    def handle(self, *args, **options):
        orders = Order.objects.all()
        if orders:
            self.stdout.write('Orders list:')
            for order in orders:
                products_details = ', '.join([f'{product} (ID: {product.id})' for product in order.products.all()])
                self.stdout.write(f'Order {order.id}: {order}')
        else:
            self.stdout.write(self.style.WARNING('No orders found.'))
