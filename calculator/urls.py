from django.urls import path
from . import views

app_name = "calculator"
urlpatterns = [
    path("", views.calulate_footprint, name="calculate_footprint"),
]