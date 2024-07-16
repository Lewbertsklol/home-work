from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.catalog.models import BaseModel
# Create your models here.


class Post(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    slug = models.CharField(max_length=255, verbose_name='slug')
    text = models.TextField(verbose_name=_('Текст'))
    preview = models.ImageField(upload_to='posts/', verbose_name=_('Превью'), blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name=_('Опубликовано'))
    views_count = models.IntegerField(default=0, verbose_name=_('Количество просмотров'))

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return self.title
