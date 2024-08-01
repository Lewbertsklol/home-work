from django.views import generic
from django.urls import reverse_lazy

from apps.catalog.models import Product
from apps.catalog.forms import ProductForm


class ProductListView(generic.ListView):
    model = Product


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(generic.DetailView):
    model = Product


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
