from django.shortcuts import render
from django.views import View
from .models import Catalog


class AboutUsView(View):
    def get(self, request):
        catalogs = Catalog.objects.all()
        return render(request, 'about_us/about_us.html', {
            'catalogs': catalogs
        })
