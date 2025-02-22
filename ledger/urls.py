from django.urls import include, path
from django.contrib import admin
from .views import recipeList, recipe1, recipe2

urlpatterns = [
    path('recipe/1/', recipe1, name = "recipe1"),
    path('recipe/2/', recipe2, name = "recipe2"),
    path('recipes/list/', recipeList, name = "recipeList")
]

app_name = "ledger"