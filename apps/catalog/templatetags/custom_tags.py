from django.template import Library

from apps.catalog.models import Product

register = Library()


@register.filter(name='img_url')
def img_url(product: Product):
    try:
        return product.image.url
    except ValueError:
        return ''


@register.filter(name='current_version_name')
def current_version_name(product: Product):
    current_version = product.versions.filter(is_current=True)
    if current_version.exists():
        current_version = current_version.first()
        return current_version.name

    return ''


@register.filter(name='current_version_number')
def current_version_name(product: Product):
    current_version = product.versions.filter(is_current=True)
    if current_version.exists():
        current_version = current_version.first()
        return current_version.number

    return ''
