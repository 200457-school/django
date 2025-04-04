from django import forms
from .models import Schedule


class DateSelectForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    schedule_type = forms.ChoiceField(choices=Schedule.SCHEDULE_TYPE, widget=forms.Select(attrs={'class': 'form-control'}))
    action = forms.ChoiceField(choices=Schedule.ACTION, widget=forms.Select(attrs={'class': 'form-control'}))