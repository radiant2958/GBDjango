from django.core.management.base import BaseCommand
from mypages.models import Product

class Command(BaseCommand):
    help = 'get product ID'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='Product ID to retrieve')

    def handle(self, *args, **options):
        product_id = options['product_id']
        try:
            product = Product.objects.get(id=product_id)
            self.stdout.write(f'Product {product_id}: {product}')
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Product not found.'))
