from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    name = models.CharField(max_length=66, verbose_name=_('نام و نام خانوادگی'))
    number = models.CharField(max_length=14, verbose_name=_('شماره تماس'))
    message = models.TextField(null=True, blank=True, verbose_name=_('پیام'))

    class Meta:
        verbose_name = _('ارتباط')
        verbose_name_plural = _('ارتباط ها')

    def __str__(self):
        return f'( {self.name} ) -- ( {self.number} )'
