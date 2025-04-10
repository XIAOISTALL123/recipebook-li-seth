from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from .views import RecipeListView, RecipeDetailView, RecipeCreateView

urlpatterns = [
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = "recipe"),
    path('recipes/list/', RecipeListView.as_view(), name = "recipes/list"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('recipe/add/', RecipeCreateView.as_view(), name = 'add'),
]

app_name = "ledger"
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
