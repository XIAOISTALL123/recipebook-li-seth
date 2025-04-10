from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from .models import Recipe, RecipeIngredient, RecipeImage

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

IngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient,
    fields = '__all__',
    extra = 1, can_delete = False
)

RecipeImageFormSet = modelformset_factory(
    RecipeImage, form = RecipeImageForm,
    extra = 1, can_delete = False
)
