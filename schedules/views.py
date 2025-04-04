from django.shortcuts import render, redirect
from .models import Schedule

from . import forms


@login_required
def date_select(request):
    if request.method == "POST":
        form = forms.DateSelectForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            schedule_type = form.cleaned_data["schedule_type"]
            action = form.cleaned_data["action"]
            return redirect("schedules:available_slots", date, schedule_type, action)

    else:
        form = forms.DateSelectForm()

    return render(request, "schedules/date_select.html", {"form": form})


@login_required
def available_slots(request, date, schedule_type, action):
    booked_time_slots = Schedule.objects.filter(date=date, schedule_type=schedule_type, action=action).values_list("time_slot", flat=True)
    available_time_slots 
    return render(request, "schedules/available_slots.html", {"date": date, "schedule_type": schedule_type, "action": action})