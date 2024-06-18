from modeltranslation.translator import TranslationOptions, translator
from .models import ConstructionCost


class ConstructionCostTranslationOptions(TranslationOptions):
    fields = (
        'concrete_roof_column_begin', 'concrete_roof_column_end', 'metal_roof_column_begin', 'metal_roof_column_end',
        'hardening_begin', 'hardening_end', 'joinery_begin', 'construction_with_materials_begin', 'construction_with_materials_end',
        'construction_without_materials_begin', 'construction_without_materials_example_begin', 'construction_without_materials_example_end',
        'created_time', 'last_prices_update',
    )


translator.register(ConstructionCost, ConstructionCostTranslationOptions)
