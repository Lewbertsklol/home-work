from django.template import Library


register = Library()


@register.filter(name='img_url')
def img_url(obj):
    try:
        return obj.image.url
    except Exception:
        return ''
