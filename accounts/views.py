from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.views import LoginView

from . import forms


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = forms.CustomAuthenticationForm
    success_url = reverse_lazy("core:home")


class UpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.UserUpdateForm(instance=request.user)
        return render(request, "accounts/update.html", {"form": form})

    def post(self, request):
        form = forms.UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("accounts:update")

        return render(request, "accounts/update.html", {"form": form})


class DeleteView(LoginRequiredMixin, View):
    def post(self, request):
        request.user.delete()
        logout(request)
        messages.success(request, "Your account has been deleted")
        return redirect("core:home")

    def get(self, request):
        return HttpResponseNotFound()


class DashboardView(LoginRequiredMixin, FormView):
    pass

