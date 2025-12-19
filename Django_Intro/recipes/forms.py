from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'type', 'description', 'video_uri', 'ingredients', 'cuisine']

        widgets = {
            'cuisine': forms.TextInput(attrs={
                'placeholder': 'e.g., British, French, Chinese, American...'
            })
        }

        labels = {
            'title': 'Title',
            'author': 'Author',
            'type': 'Type',
            'description': 'Description',
            'video_uri': 'Video URI',
            'ingredients': 'Ingredients',
            'cuisine': 'Cuisine',
        }