from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Usage
from .forms import UsageForm


@login_required
def calculate(request):
    if request.method == "POST":
        form = UsageForm(request.POST)
        if form.is_valid():
            electricity = form.cleaned_data["electricity"]
            gas = form.cleaned_data["gas"]
            water = form.cleaned_data["water"]

            Usage.objects.create(
                user=request.user,
                electricity=electricity,
                gas=gas,
                water=water,
            )

            return redirect("energy_usage:dashboard")

    else:
        form = UsageForm()

    return render(request, "energy_usage/calculate.html", {"form": form})


@login_required
def dashboard(request):
    user = request.user
    usages = Usage.objects.filter(user=user).order_by("-date")

    return render(request, "energy_usage/dashboard.html", {"usages": usages})