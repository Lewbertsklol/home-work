from django.core.management.base import BaseCommand
from django.core.management import call_command

from apps.catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Initialize database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        call_command('loaddata', './apps/catalog/fixtures/catalog_data.json')
