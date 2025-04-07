from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = "recipe"),
    path('recipes/list/', RecipeListView.as_view(), name = "recipes/list"),
    path('accounts/login/', LoginView.as_view(), name='login')
]

app_name = "ledger"