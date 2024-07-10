from django.template import Library


register = Library()


@register.filter(name='img_url')
def img_url(obj):
    try:
        return obj.image.url
    except Exception:
        return ''


@register.inclusion_tag('catalog/includes/card.html')
def card(product):
    return {'product': product}