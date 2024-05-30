from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'index/index.html',)


class IpsSpacesFacadeDetailsView(View):
    def get(self, request):
        return render(request, 'index/ips_spaces_facade_details.html')


class IpsSpacesRestaurantDetailsView(View):
    def get(self, request):
        return render(request, 'index/ips_spaces_restaurant_details.html')


class IpsSpacesHomeDetailsView(View):
    def get(self, request):
        return render(request, 'index/ips_spaces_home_details.html')


class IpsSpacesOfficeDetailsView(View):
    def get(self, request):
        return render(request, 'index/ips_spaces_office_details.html')
