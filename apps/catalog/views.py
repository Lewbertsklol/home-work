from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
# Create your views here.

from .forms import ProductForm
from .models import Product, Version


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = {
            'versions': Version.objects.all(),
        }
        return super().get_context_data(**kwargs, **context)


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(generic.DetailView):
    model = Product


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class FeedbackView(generic.View):

    def get(self, request):
        return render(request, 'catalog/feedback.html')

    def post(self, request):
        return redirect('catalog:product_list')
