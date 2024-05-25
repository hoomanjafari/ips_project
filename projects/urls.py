from django.urls import path
from . import views


app_name = 'ips-projects'
urlpatterns = [
    path('', views.IpsProjectsView.as_view(), name='ips-projects'),
    path('projects_filtering/', views.IpsProjectFilteringView.as_view(), name='projects-filtering'),
    path('filtering_template_change/', views.FilterChangeTemplate.as_view(), name='filtering-template-change'),
]
