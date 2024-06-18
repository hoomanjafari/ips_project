from django.urls import path
from . import views


app_name = 'construction-cost'
urlpatterns = [
    path('', views.ConstructionCostView.as_view(), name='construction-cost')
]
