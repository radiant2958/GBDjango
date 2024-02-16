from django.core.management.base import BaseCommand
from mypages.models import Product  

class Command(BaseCommand):
    help = 'Creates a new product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **options):
        product = Product.objects.create(
            name=options['name'],
            description=options['description'],
            price=options['price'],
            quantity=options['quantity']
        )
        self.stdout.write(f'{product}')
