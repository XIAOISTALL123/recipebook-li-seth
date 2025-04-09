from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient, Recipe, RecipeIngredient
from .forms import RecipeCreateForm

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipeList.html' 
    redirect_field_name = 'accounts/login'
    
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html' 
    redirect_field_name = 'accounts/login'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipeCreate.html'
    redirect_field_name = 'accounts/login'