from  django import forms
from .models import Car

class CarForms(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name_car', 'category', 'marka', 'model', 'description', 'price', 'image', 'year']