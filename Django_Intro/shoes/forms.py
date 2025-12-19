from django import forms
from .models import Shoe


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['manufacture', 'gender', 'type', 'color', 'size', 'price']

        widgets = {
            'manufacture': forms.TextInput(attrs={
                'placeholder': 'e.g., Nike, Adidas, Puma...'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
        }

        labels = {
            'manufacture': 'Manufacturer / Brand',
            'gender': 'Gender',
            'type': 'Type',
            'color': 'Color',
            'size': 'Size',
            'price': 'Price (USD)',
        }