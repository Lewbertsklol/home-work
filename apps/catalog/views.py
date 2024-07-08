from django.shortcuts import render

# Create your views here.

from .models import Product


def index_view(request):
    product_list = Product.objects.all()
    return render(request, 'catalog/index.html', {
        'product_list': product_list
    })


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalog/product.html', {
        'product': product
    })


def feedback_view(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'catalog/feedback.html')
