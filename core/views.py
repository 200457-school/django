from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from schedules.models import Schedule
from energy_usage.models import Usage


@login_required
def dashboard(request):
    user = request.user
    usages = Usage.objects.filter(user=user).order_by("-date")
    installations = Schedule.objects.filter(user=request.user, action="I")
    consultations = Schedule.objects.filter(user=request.user, action="C")

    return render(request, "core/dashboard.html", {
        "usages": usages,
        "installations": installations,
        "consultations": consultations
    })