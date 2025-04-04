from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "accounts"
urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("update/", views.UpdateView.as_view(), name="update"),
    path("update/delete/", views.DeleteView.as_view(), name="delete"),
]