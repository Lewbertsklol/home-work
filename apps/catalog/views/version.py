from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect

from apps.catalog.models import Product, Version


class VersionListView(generic.ListView):
    model = Version

    def get_queryset(self):
        return Version.objects.filter(product__pk=self.kwargs['product_pk'])

    def get_context_data(self, **kwargs):
        return super().get_context_data(product_pk=self.kwargs['product_pk'], **kwargs)


class VersionCreateView(generic.CreateView):
    model = Version
    fields = ('name', 'number', 'is_current')

    def form_valid(self, form):
        form.instance.product = Product.objects.get(pk=self.kwargs['product_pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:version_list', kwargs={'product_pk': self.kwargs['product_pk']})


class VersionDeleteView(generic.DeleteView):
    model = Version

    def get_success_url(self):
        return reverse('catalog:version_list', kwargs={'product_pk': self.object.product.pk})


def toggle_current_version(request, pk):
    version = Version.objects.get(pk=pk)
    version.is_current = not version.is_current
    version.save()
    return redirect('catalog:version_list', product_pk=version.product.pk)
