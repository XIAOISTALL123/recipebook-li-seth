"""This file contains the models for the recipebook."""
from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    """Model for a single ingredient."""
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ingredients', args[str(self.name)])

class Recipe(models.Model):
    """Model for a recipe."""
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])

class RecipeIngredient(models.Model):
    """Model for an ingredient in a recipe."""
    quantity = models.CharField(max_length = 255)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE, related_name = "recipe")
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name = "ingredients")
