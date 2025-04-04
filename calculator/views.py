from django.shortcuts import render
from .forms import CarbonFootprintForm
from .utils import calculate_co2_emissions

def calulate_footprint(request):
    if request.method == 'POST':
        form = CarbonFootprintForm(request.POST)
        if form.is_valid():
            transportation_km = form.cleaned_data['transportation_km']
            energy_consumption_kWh = form.cleaned_data['energy_kWh']
            waste_generation_kg = form.cleaned_data['waste_kg']
            
            co2_emissions = calculate_co2_emissions(
                transportation_km, energy_consumption_kWh, waste_generation_kg
            )
            
            return render(request, 'calculator/result.html', {'co2_emissions': co2_emissions})
    else:
        form = CarbonFootprintForm()
    
    return render(request, 'calculator/calculate.html', {'form': form})