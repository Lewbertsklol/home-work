from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.catalog.models import Product
from apps.catalog.forms import ProductForm
from apps.users.permissions import EmailVerifiedRequiredMixin


class ProductListView(generic.ListView):
    model = Product


class ProductCreateView(LoginRequiredMixin, EmailVerifiedRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, EmailVerifiedRequiredMixin, generic.DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, EmailVerifiedRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
