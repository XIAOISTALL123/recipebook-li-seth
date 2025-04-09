"""This file contains the models for the recipebook."""
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    bio = models.CharField(max_length = 255)

class Ingredient(models.Model):
    """Model for a single ingredient."""
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ingredients', args[str(self.name)])

class Recipe(models.Model):
    """Model for a recipe."""
    name = models.CharField(max_length = 255, null = True)
    author = models.CharField(max_length = 50, null = True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])

class RecipeIngredient(models.Model):
    """Model for an ingredient in a recipe."""
    quantity = models.CharField(max_length = 255)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE, related_name = "recipe")
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = "ingredients")

class RecipeImage(models.Model):
    image = models.ImageField(upload_to = "images/", null = False)
    description = models.CharField(max_length = 255, null = True)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = "image")