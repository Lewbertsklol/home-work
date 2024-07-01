from django.db import models
from django.utils.translation import gettext_lazy as _

from .basemodel import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name
