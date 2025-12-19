from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'photo_url', 'rating']

        labels = {
            'title': 'Title',
            'price': 'Price',
            'description': 'Description',
            'photo_url': 'Photo URL',
            'rating': 'Rating'
        }