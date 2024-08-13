from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from apps.catalog.models.product import Product


class Command(BaseCommand):
    help = 'Create moderator group'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=(
                'can_change_published',
                'can_change_description',
                'can_change_category'
            ),
        )
        group = Group.objects.create(name='moderator')
        group.permissions.set(permissions)
        print('Moderator group have been created.')
