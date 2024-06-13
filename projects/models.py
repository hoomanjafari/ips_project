from django.db import models
from django.utils.translation import gettext_lazy as _


class IpsProjects(models.Model):
    project_title = models.CharField(max_length=30, verbose_name=_('عنوان پروژه'))
    project_time_city = models.CharField(max_length=33, verbose_name=_('سال و شهر'))
    project_address = models.CharField(max_length=66, verbose_name=_('ادرس پروژه'))
    project_main_image = models.ImageField(upload_to='img/%y%m%d%H%M', verbose_name=_('عکس اصلی پروژه'))
    project_details = models.TextField(verbose_name=_('توضیحات پروژه'))
    created = models.DateTimeField(auto_now_add=True)

    is_home_villa = models.BooleanField(default=False, verbose_name=_('خانه و ویلا'))
    is_facade = models.BooleanField(default=False, verbose_name=_('نما سازی'))
    is_zero_to_hundred = models.BooleanField(default=False, verbose_name=_('صفر تا صد'))
    is_coffe_restaurant = models.BooleanField(default=False, verbose_name=_('رستوران و کافه'))
    is_office = models.BooleanField(default=False, verbose_name=_('محل کار'))

    project_img_1 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True, verbose_name=_('عکس 1'))
    project_img_2 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True, verbose_name=_('عکس 2'))
    project_img_3 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True, verbose_name=_('عکس 3'))
    project_img_4 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True, verbose_name=_('عکس 4'))
    project_img_5 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True, verbose_name=_('عکس 5'))
    project_img_6 = models.ImageField(upload_to='img/%y%m%d%H%M', null=True, blank=True, verbose_name=_('عکس 6'))

    class Meta:
        verbose_name_plural = _('پروژه ها')
        verbose_name = _('پروژه')

    def __str__(self):
        return f'{self.project_title} {self.project_time_city}'