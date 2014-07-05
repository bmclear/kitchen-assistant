from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from kitchen.models import Ingredient
from kitchen.forms import UserForm, UserProfileForm

from datetime import datetime

@login_required
def index(request):
    context = RequestContext(request)
    current_user = request.user

    if current_user.username == "kirk":
        temp = "You are 'kirk'."
    else:
        temp = "You are NOT 'kirk'."

    context_dict = {}
    context_dict['temp'] = temp

    return render_to_response("kitchen/index.html", context_dict, context)

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
