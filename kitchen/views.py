from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from kitchen.models import Ingredient

from datetime import datetime

@login_required
def index(request):
    context = RequestContext(request)
    return render_to_response("kitchen/index.html", {}, context)

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
