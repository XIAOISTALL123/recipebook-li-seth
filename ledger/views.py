from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipeList.html' 
    
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html' 
    redirect_field_name = 'accounts/login'


