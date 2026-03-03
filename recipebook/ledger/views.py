from .models import Recipe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.recipe_ingredients.all()
    author = recipe.author
    ctx = {"name": recipe, "ingredients": ingredients, "author": author}
    return render(request, "./recipes/recipe.html", ctx)


def recipe_list(request):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(request, "./recipes/recipe_list.html", ctx)
