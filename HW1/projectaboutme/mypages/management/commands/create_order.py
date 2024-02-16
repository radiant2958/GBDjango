from django.core.management.base import BaseCommand
from mypages.models import Order, Client, Product  


class Command(BaseCommand):
    help = 'Creates a new order'

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='Customer ID')
        parser.add_argument('product_ids', nargs='+', type=int, help='List of product IDs')

    def handle(self, *args, **options):
        customer = Client.objects.get(id=options['customer_id'])
        
        # Инициализация переменной для общей цены
        total_price = 0  

        # Подсчет общей цены на основе выбранных продуктов
        for product_id in options['product_ids']:
            product = Product.objects.get(id=product_id)
            total_price += product.price  # Суммирование цен продуктов

        # Создание заказа с вычисленной общей ценой
        order = Order.objects.create(customer=customer, total_price=total_price)

        # Добавление продуктов к заказу
        for product_id in options['product_ids']:
            order.products.add(product_id)
        
        order.save()


        self.stdout.write(f'{order}')
