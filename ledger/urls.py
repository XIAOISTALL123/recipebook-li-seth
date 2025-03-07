from django.urls import include, path
from django.contrib import admin
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = "recipe"),
    path('recipes/list/', RecipeListView.as_view(), name = "recipes/list")
]

app_name = "ledger"