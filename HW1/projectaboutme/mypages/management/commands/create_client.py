from django.core.management.base import BaseCommand
from mypages.models import Client

class Command(BaseCommand):
    help = "Create a new client"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone', type=str, help='Client phone number')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **options):
        name = options['name']
        email = options['email']
        phone = options['phone']
        address = options['address']
        client = Client(name=name, email=email, phone=phone, address=address)
        client.save()
        self.stdout.write(f'{client}')