from django.core.management.base import BaseCommand
from mypages.models import Client

class Command(BaseCommand):
    help = 'all clients'

    def handle(self, *args, **options):
        clients = Client.objects.all()
        if clients:
            self.stdout.write('Clients list:')
            for client in clients:
                self.stdout.write(f'{client.id}: {client}')
        else:
            self.stdout.write(self.style.WARNING('No clients found.'))
