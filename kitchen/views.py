from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from kitchen.models import Ingredient, UserIngredient, UserRecipe
from kitchen.forms import UserForm, UserProfileForm, IngredientForm, RecipeForm

from datetime import datetime

@login_required
def index(request):
    context = RequestContext(request)
    current_user = request.user

    user_ingredients = UserIngredient.objects.filter(user=current_user)
    context_dict = {}
    context_dict['ingredients'] = user_ingredients
    
    user_recipes = UserRecipe.objects.filter(user=current_user)
    context_dict['recipes'] = user_recipes

    return render_to_response("kitchen/new_index.html", context_dict, context)

def user_login(request):
    context = RequestContext(request)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/kitchen/")
            else:
                return HttpResponse("Your account is currently disabled.")
        else:
            print "Invalid username or password."
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response("kitchen/login.html", {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/kitchen/")

@login_required
def add_ingredient(request):
    context = RequestContext(request)

    if request.method == "POST":
        ingredient_form = IngredientForm(data=request.POST)

        if ingredient_form.is_valid():
            new_ingredient = ingredient_form.save(commit=False)
            new_ingredient.user = request.user
            new_ingredient.save()
            return HttpResponseRedirect("/kitchen/")
        else:
            print ingredient_form.errors
    else:
        ingredient_form = IngredientForm()

    return render_to_response("kitchen/add_ingredient.html", {'ingredient_form': ingredient_form,}, context)

@login_required
def add_recipe(request):
    context = RequestContext(request)

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)

        if recipe_form.is_valid():
            new_recipe = recipe_form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            return HttpResponseRedirect("/kitchen/")
        else:
            print recipe_form.errors
    else:
        recipe_form = RecipeForm()

    return render_to_response("kitchen/new_add_recipe.html", {'recipe_form': recipe_form,}, context)

def user_register(request):
    context = RequestContext(request)

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "picture" in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response("kitchen/register.html",
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

@login_required
def browse_recipes(request):
    context = RequestContext(request)

    recipes = UserRecipe.objects.filter(user=request.user)
    context_dict = {'recipes': recipes}

    return render_to_response("kitchen/browse_recipes.html", context_dict, context)

@login_required
def shopping_list(request):
    context = RequestContext(request)

    return render_to_response("kitchen/shopping_list.html", {}, context)

@login_required
def what_make(request):
    context = RequestContext(request)

    return render_to_response("kitchen/what_make.html", {}, context)
