from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from recipes_app.models import Recipe
from recipes_app.forms import CreateRecipe


# Create your views here.
def homepage(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create(request):
    context = {}
    if request.method == 'POST':
        form = CreateRecipe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreateRecipe(label_suffix='')
    context = {'form': form}
    return render(request, 'create.html', context)


def edit(request, rec_id):
    context = {}
    try:
        recipe = Recipe.objects.get(pk=rec_id)
    except ObjectDoesNotExist:
        return redirect('homepage')

    if request.method == 'POST':
        form = CreateRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreateRecipe(instance=recipe)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete(request, rec_id):
    context = {}
    try:
        recipe = Recipe.objects.get(pk=rec_id)
    except ObjectDoesNotExist:
        return redirect('homepage')
    if request.method == 'POST':
        recipe.delete()
        return redirect('homepage')
    else:
        form = CreateRecipe(instance=recipe)
        for field in form.fields:
            form.fields[field].disabled = True
    context = {
        'form': form
    }
    return render(request, 'delete.html',context)


def details(request, rec_id):
    context = {}
    try:
        recipe = Recipe.objects.get(pk=rec_id)
    except ObjectDoesNotExist:
        return redirect('homepage')
    ingredients_list = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'list': ingredients_list
    }
    return render(request, 'details.html',context)
