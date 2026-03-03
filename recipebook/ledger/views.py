from .models import Recipe
from django.shortcuts import render


def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.recipe_ingredients.all()
    ctx = {"name": recipe, "ingredients": ingredients}
    return render(request, "./recipes/recipe.html", ctx)


def recipe_list(request):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(request, "./recipes/recipe_list.html", ctx)
