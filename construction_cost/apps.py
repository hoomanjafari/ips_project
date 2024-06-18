from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConstructionCostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'construction_cost'
    verbose_name = _('قیمت ساختمان سازی')
