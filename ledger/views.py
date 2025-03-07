from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipeList.html' 
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html' 


