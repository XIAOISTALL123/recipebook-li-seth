from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient, Recipe, RecipeIngredient
from .forms import RecipeCreateForm, IngredientFormSet

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = IngredientFormSet(self.request.POST)
        else:
            context['formset'] = IngredientFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            ingredients = formset.save(commit = False)
            for ingredient in ingredients:
                ingredient.recipe = self.object
                ingredient.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)