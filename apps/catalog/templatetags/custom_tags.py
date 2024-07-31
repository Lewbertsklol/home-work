from django.template import Library


register = Library()


@register.filter(name='img_url')
def img_url(obj):
    try:
        return obj.image.url
    except Exception:
        return ''

@register.filter(name='current_version_name')
def current_version_name(obj):
    return 'obj.versions.filter(is_current=True).first().name'