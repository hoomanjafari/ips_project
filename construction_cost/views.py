from django.shortcuts import render
from django.views import View
from .models import ConstructionCost


class ConstructionCostView(View):
    def get(self, request):
        construction = ConstructionCost.objects.get(pk=1)
        return render(request, 'construction_cost/construction_cost.html', {
            'construction': construction
        })
