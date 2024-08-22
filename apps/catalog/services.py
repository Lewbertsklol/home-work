from django.core.cache import cache
from django.db.models import QuerySet

from .models import Category
from config.settings import CACHE_ENABLED


def get_cached_list_categories() -> QuerySet[Category]:
    return cache.get_or_set(
        key='category_list',
        default=Category.objects.all(),
        timeout=60
    ) if CACHE_ENABLED else Category.objects.all()
