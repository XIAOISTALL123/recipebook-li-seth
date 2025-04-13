from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Recipe, RecipeImage, Ingredient
from .forms import RecipeCreateForm, RecipeImageForm, IngredientFormSet, RecipeImageFormSet, IngredientCreateForm, IngredientCreateFormSet

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
        form.instance.author = self.request.user.username
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save()
            ingredients = formset.save(commit = False)
            
            for ingredient in ingredients:
                ingredient.recipe = self.object
                ingredient.save()
            return redirect(self.get_success_url())
        return self.form_invalid(form)

class RecipeImageAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeImageForm 
    template_name = 'recipeImage.html'
    redirect_field_name = 'accounts/login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['image_formset'] = RecipeImageFormSet(self.request.POST, self.request.FILES,
                                                            queryset = RecipeImage.objects.none())
        else:
            context['image_formset'] = RecipeImageFormSet(queryset = RecipeImage.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']

        if image_formset.is_valid():
            recipe = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))

            for image_form in image_formset:
                if image_form.cleaned_data:
                    image = image_form.save(commit = False)
                    image.recipe = recipe
                    image.save()

            return redirect(recipe.get_absolute_url())
        return self.form_invalid(form)

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.required = False
        return form 

class IngredientAddView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = 'ingredientCreate.html'
    redirect_field_name = 'accounts/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = IngredientCreateFormSet(self.request.POST, queryset = Ingredient.objects.none())
        else:
            context['formset'] = IngredientCreateFormSet(queryset = Ingredient.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            formset.save()
            return redirect(reverse("ledger:recipes/list"))
        return self.form_invalid(form)

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.required = False
        return form
