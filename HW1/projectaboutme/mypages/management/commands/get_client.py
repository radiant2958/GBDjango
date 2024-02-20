from django.core.management.base import BaseCommand
from mypages.models import Client

class Command(BaseCommand):
    help = 'get client ID'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID to retrieve')

    def handle(self, *args, **options):
        client_id = options['client_id']
        try:
            client = Client.objects.get(id=client_id)
            self.stdout.write(f'Client {client_id}: {client}')
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR('Client not found.'))
