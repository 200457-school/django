from django import forms

class CarbonFootprintForm(forms.Form):
    transportation_km = forms.FloatField(label='Transportation Distance (km)', min_value=0)
    energy_kWh = forms.FloatField(label='Energy Consumption (kWh)', min_value=0)
    waste_kg = forms.FloatField(label='Waste Generation (kg)', min_value=0)