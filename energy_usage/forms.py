from .models import Usage
from django import forms  


class UsageForm(forms.ModelForm):
    class Meta:
        model = Usage
        fields = ["electricity", "gas", "water"]