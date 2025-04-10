from django import forms
from .models import Recipe, RecipeIngredient
from django.forms import inlineformset_factory

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

IngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient,
    fields = '__all__',
    extra = 1, can_delete = False
)