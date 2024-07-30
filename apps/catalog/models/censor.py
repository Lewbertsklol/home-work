from django.db import models
from django.utils.translation import gettext_lazy as _

from .basemodel import BaseModel


class Censor(BaseModel):
    word = models.CharField(max_length=255, verbose_name=_('Слово'))

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = _('Цензура')
        verbose_name_plural = _('Цензура')
