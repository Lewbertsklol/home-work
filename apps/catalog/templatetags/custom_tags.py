from django.template import Library


register = Library()


@register.filter(name='img_url')
def img_url(obj):
    try:
        return obj.image.url
    except Exception:
        return ''


@register.filter(name='current_version_info')
def current_version_name(obj):
    current_version = obj.versions.filter(is_current=True)
    if current_version.exists():
        current_version = current_version.first()
        return f'Версия № {current_version.number}: {current_version.name}'

    return ''
