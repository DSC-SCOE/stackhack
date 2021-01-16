from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, authenticate, logout

from django.views.decorators.csrf import csrf_exempt

from mainApp import forms as modelForms
from api import models as apiModels

from django.contrib.auth.hashers import make_password

import json
import requests


def Logout(request):
    logout(request)
    return HttpResponse("<h1>logout</h1>")


def signUp(request):
    if request.method == "POST":
        form = modelForms.signupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            if data['password1'] == data['password2']:
            
                data2 = {
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'email': data['email'],
                    'username': data['username'],
                    'password': make_password(data['password1'])
                }
                print(data2)

                jsondata = json.dumps(data2)

                URL = "http://127.0.0.1:8000/api/user/"

                r = requests.post(url= URL, data= jsondata)

                if r.status_code == 200:
                    return HttpResponse(r)
                else:
                    return HttpResponse(r)

            return HttpResponse("<h1>Employee added</h1>")
    else:

        form = modelForms.signupForm()

    return render(
        request,
        "test.html",
        {
            "form": form,
        },
    )


def Login(request):
    if request.user.is_authenticated:
        return redirect("dashboard/")
    else:
        if request.method == "POST":
            uname = request.POST["username"]
            upass = request.POST["password"]

            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)

                return redirect("dash")

        form = AuthenticationForm()
        return render(
            request,
            "test.html",
            {
                "form": form,
            },
        )


def dash(request):
    if request.user.is_authenticated:
        form = modelForms.empForm()

        return render(
            request,
            "test.html",
            {
                "form": form,
            },
        )
