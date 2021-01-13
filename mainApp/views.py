from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, authenticate, logout

from django.views.decorators.csrf import csrf_exempt

from mainApp import forms as modelForms
from api import models as apiModels


import json
import requests


def Logout(request):
    logout(request)
    return HttpResponse('<h1>logout</h1>')


def signUp(request):
    
    if request.method == "POST":
        form = modelForms.signupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            """ jsondata = json.dumps(data)

            URL = "http://127.0.0.1:8000/api/addEmp/"

            r = requests.post(url= URL, data= jsondata) """

            form.save()

            uname = data['username']
            upass = data['password1']

            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)
                
                return redirect('dashboard/')

            return HttpResponse('<h1>Employee added</h1>')
            
            #return HttpResponse('<h1>error occured</h1>')
    else :
    
        form = modelForms.signupForm()
    
    return render(request, 'test.html', {
        'form':form,
    })


def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard/')
    else:
        if request.method == "POST":
            uname = request.POST['username']
            upass = request.POST['password']

            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)

                return redirect('dash')
            

        form = AuthenticationForm()
        return render(request, 'test.html', {
            'form':form,
        })


def dash(request):
    if request.user.is_authenticated:
        form = modelForms.empForm()

        return render(request, 'test.html', {
            'form':form,
        })
