from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Schedule
from django.contrib.auth.mixins import LoginRequiredMixin


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
    available_time_slots = set(range(0, 8)) - set(booked_time_slots)
    user_friendly_slots = [
        {"value": slot, "label": dict(Schedule.TIME_SLOT)[slot]}
        for slot in available_time_slots
    ]

    return render(request, "schedules/available_slots.html", {
        "time_slots": user_friendly_slots,
        "date": date,
        "schedule_type": schedule_type,
        "action": action,
    })


@login_required
def book(request, date, schedule_type, action, time_slot):
    if request.method == "POST":
        Schedule.objects.create(
            user=request.user,
            schedule_type=schedule_type,
            action=action,
            time_slot=time_slot,
            date=date,
        )
        return redirect("schedules:dashboard")