from django.db import models
from django.utils.translation import gettext_lazy as _

from .basemodel import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to='products/', verbose_name=_('Изображение'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Категория'))
    price = models.FloatField(verbose_name=_('Цена'))

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    def __str__(self):
        return self.name
