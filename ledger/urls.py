from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView
from .views import RecipeListView, RecipeDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = "recipe"),
    path('recipes/list/', RecipeListView.as_view(), name = "recipes/list"),
    path('accounts/login/', LoginView.as_view(), name='login')
]

app_name = "ledger"

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)