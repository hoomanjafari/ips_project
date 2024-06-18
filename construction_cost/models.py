from django.db import models
from django.utils.translation import gettext_lazy as _


class ConstructionCost(models.Model):
    last_prices_update = models.CharField(
        max_length=33, verbose_name=_('اخرین بروز رسانی'), null=True, blank=True
    )

    concrete_roof_column_begin = models.CharField(
        max_length=33, verbose_name=_('شروع سقف و ستون بتنی'), null=True, blank=True
    )
    concrete_roof_column_end = models.CharField(
        max_length=33, verbose_name=_('پایان سقف و ستون بتنی'), null=True, blank=True
    )

    metal_roof_column_begin = models.CharField(
        max_length=33, verbose_name=_('َشروع سقف و ستون فلزی'), null=True, blank=True
    )
    metal_roof_column_end = models.CharField(
        max_length=33, verbose_name=_('پایان سقف و ستون فلزی'), null=True, blank=True
    )

    hardening_begin = models.CharField(
        max_length=33, verbose_name=_('شروع سفت کاری'), null=True, blank=True
    )
    hardening_end = models.CharField(
        max_length=33, verbose_name=_('پایان سفت کاری'), null=True, blank=True
    )

    joinery_begin = models.CharField(
        max_length=33, verbose_name=_('شروع نازک کاری'), null=True, blank=True
    )

    construction_with_materials_begin = models.CharField(
        max_length=33, verbose_name=_('شروع ساختمان سازی با مصالح'), null=True, blank=True
    )
    construction_with_materials_end = models.CharField(
        max_length=33, verbose_name=_('پایان ساختمان سازی با مصالح'), null=True, blank=True
    )

    construction_without_materials_begin = models.CharField(
        max_length=33, verbose_name=_('شروع ساختمان سازی بدون مصالح'), null=True, blank=True
    )
    construction_without_materials_example_begin = models.CharField(
        max_length=33, verbose_name=_('مثال شروع ساختمان سازی بدون مصالح'), null=True, blank=True
    )
    construction_without_materials_example_end = models.CharField(
        max_length=33, verbose_name=_('مثال پایان ساختمان سازی بدون مصالح'), null=True, blank=True
    )

    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('قیمت های ساختمان سازی')
        verbose_name = _('قیمت ساختمان سازی')

    def __str__(self):
        return f'{self.created_time} -- id : {self.id} '
