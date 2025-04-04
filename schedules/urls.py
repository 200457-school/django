from django.urls import path

from . import views

app_name = "schedules"
urlpatterns = [
    path("select_date/", views.date_select, name="date_select"),
    path("available_slots/<str:date>/<str:schedule_type>/<str:action>/", views.available_slots, name="available_slots"),
    path("book/<str:date>/<str:schedule_type>/<str:action>/<int:time_slot>/", views.book, name="book"),
    path("dashboard/", views.dashboard, name="dashboard"),
]