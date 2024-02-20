from django.core.management.base import BaseCommand
from mypages.models import Product

class Command(BaseCommand):
    help = 'all products'

    def handle(self, *args, **options):
        products = Product.objects.all()
        if products:
            self.stdout.write('Products list:')
            for product in products:
                self.stdout.write(f'{product.id}: {product}')
        else:
            self.stdout.write(self.style.WARNING('No products found.'))
