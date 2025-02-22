from django.shortcuts import render
from django.http import HttpResponse

ctx_recipeList = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quanity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}

ctx_recipe1 = {
    "name": "Recipe 1",
    "ingredients": [
        {
            "name": "tomato",
            "quantity": "3pcs"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "pork",
            "quantity": "1kg"
        },
        {
            "name": "water",
            "quantity": "1L"
        },
        {
            "name": "sinigang mix",
            "quantity": "1 packet"
        }
    ],
    "link": "/recipe/1"
}

ctx_recipe2 ={
    "name": "Recipe 2",
    "ingredients": [
        {
            "name": "garlic",
            "quantity": "1 head"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "vinegar",
            "quantity": "1/2cup"
        },
        {
            "name": "water",
            "quantity": "1 cup"
        },
        {
            "name": "salt",
            "quantity": "1 tablespoon"
        },
        {
            "name": "whole black peppers",
            "quantity": "1 tablespoon"
        },
        {
            "name": "pork",
            "quantity": "1 kilo"
        }
    ],
    "link": "/recipe/2"
}

def recipeList(request):
    return render(request, 'recipeList.html', ctx_recipeList)

def recipe1(request):   
    return render(request, 'recipe.html', ctx_recipe1)
    
def recipe2(request):   
    return render(request, 'recipe.html', ctx_recipe2)


# Create your views here.
