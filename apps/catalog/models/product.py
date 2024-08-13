from django.db import models
from django.utils.translation import gettext_lazy as _

from .basemodel import BaseModel


class Product(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name=_('Изображение'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Категория'))
    price = models.FloatField(verbose_name=_('Цена'))
    is_published = models.BooleanField(default=False, verbose_name=_('Опубликовано'))

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')
        permissions = [
            ("can_change_published", "Can change is_published status"),
            ("can_change_description", "Can change description"),
            ("can_change_category", "Can change category"),
        ]

    def __str__(self):
        return self.name
