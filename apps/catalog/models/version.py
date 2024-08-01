from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .basemodel import BaseModel


class Version(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Название версии'))
    number = models.IntegerField(unique=True, verbose_name=_('Номер версии'))
    is_current = models.BooleanField(default=True, verbose_name=_('Текущая версия'))
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name=_('Продукт'), related_name='versions')

    class Meta:
        verbose_name = _('Версия продукта')
        verbose_name_plural = _('Версии продукта')
        ordering = ['number']

    def __str__(self):
        return f'{self.number}. {self.name} ({self.is_current})'


@receiver(pre_save, sender=Version)
def pre_save_version(sender, instance, **kwargs):
    Version.objects.filter(product=instance.product, is_current=True).update(is_current=False)


@receiver(post_delete, sender=Version)
def post_delete_version(sender, instance, **kwargs):
    if instance.is_current:
        previous_versions = Version.objects.filter(product__pk=instance.product.pk)
        if previous_versions.exists():
            previous_version = previous_versions.latest('number')
            previous_version.is_current = True
            previous_version.save()
