from django.urls import path
from . import views

app_name = "energy_usage"
urlpatterns = [
    path("calculate/", views.calculate, name="calculate"),
    path("dasboard/", views.dashboard, name="dashboard"),
]