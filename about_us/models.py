from django.db import models
from django.utils.translation import gettext_lazy as _


class Catalog(models.Model):
    image = models.ImageField(upload_to='catalog_img/%y%m%d%H%M', verbose_name=_('عکس کاتالوگ'))

    class Meta:
        verbose_name = _('کاتالوک')
        verbose_name_plural = _('کاتالوگ ها')