"""This file contains the models for the recipebook."""
from django.db import models

class Ingredient(models.Model):
    """Model for a single ingredient."""
    name = models.CharField(max_length = 255)

class Recipe(models.Model):
    """Model for a recipe."""
    name = models.CharField(max_length = 255)

class RecipeIngredient(models.Model):
    """Model for an ingredient in a recipe."""
    quantity = models.CharField(max_length = 255)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
