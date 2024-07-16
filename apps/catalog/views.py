from django.views import generic
from django.shortcuts import redirect, render
# Create your views here.

from .models import Product


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product


class FeedbackView(generic.View):

    def get(self, request):
        return render(request, 'catalog/feedback.html')

    def post(self, request):
        print(request.POST)
        return redirect('catalog:product_list')
