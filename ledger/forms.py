from django import forms
from .models import Recipe

class RecipeCreateForm(forms.ModelForm):
    class Create:
        model = Recipe
        fields = ['name', 'author']