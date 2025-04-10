from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeCreateForm, IngredientFormSet, RecipeImageFormSet

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
            context['image_formset'] = RecipeImageFormSet(self.request.POST, self.request.FILES,
                                                            queryset = RecipeImage.objects.none())
        else:
            context['formset'] = IngredientFormSet()
            context['image_formset'] = RecipeImageFormSet(queryset = RecipeImage.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        image_formset = context['image_formset']
        if formset.is_valid() and image_formset.is_valid():
            self.object = form.save()
            ingredients = formset.save(commit = False)
            for ingredient in ingredients:
                ingredient.recipe = self.object
                ingredient.save()
            for image_form in image_formset:
                if image_form.cleaned_data:
                    image = image_form.save(commit = False)
                    image.recipe = self.object
                    image.save()
            return redirect(self.get_success_url())
        return self.form_invalid(form)
