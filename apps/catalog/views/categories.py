from django.views import generic

from apps.catalog.models import Category
from apps.catalog.services import get_cached_list_categories


class CategoryListView(generic.ListView):
    model = Category
    queryset = get_cached_list_categories()
