from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    path('articles/carbon-footprint/', TemplateView.as_view(template_name='core/carbon_footprint.html'), name='footprint-info'),
    path('articles/green-energy/', TemplateView.as_view(template_name='core/green_energy.html'), name='green-info'),
]