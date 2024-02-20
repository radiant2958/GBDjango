from django.core.management.base import BaseCommand
from mypages.models import Order

class Command(BaseCommand):
    help = 'get order ID'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID to retrieve')

    def handle(self, *args, **options):
        order_id = options['order_id']
        try:
            order = Order.objects.get(id=order_id)
            products_details = ', '.join([f'Product ID: {product.id}, {product.name}' for product in order.products.all()])
            self.stdout.write(f'Order {order_id}: {order}')
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR('Order not found.'))
