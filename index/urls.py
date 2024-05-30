from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('ips-spaces_facade/', views.IpsSpacesFacadeDetailsView.as_view(), name='ips-spaces-facade'),
    path('ips-spaces-restaurant/', views.IpsSpacesRestaurantDetailsView.as_view(), name='ips-spaces-restaurant'),
    path('ips-spaces-home/', views.IpsSpacesHomeDetailsView.as_view(), name='ips-spaces-home'),
    path('ips-spaces-office/', views.IpsSpacesOfficeDetailsView.as_view(), name='ips-spaces-office')
]
