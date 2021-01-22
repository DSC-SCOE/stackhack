from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

from mainApp import forms as modelForms
from api import models as apiModels

from django.contrib.auth.hashers import make_password

import json
import requests

import datetime

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
        return redirect("dash")
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
        
        if request.user.is_superuser == True:
            emps = apiModels.empList.objects.all().filter(status=False)
            print('emp data ####')
            print(emps)
            return render(request, 'admin.html', {
                'data':emps,
            })

        count = apiModels.empData.objects.filter(eid=request.user.id).count()
        print(count)
        if count < 1:
            return redirect('edit_profile')
        else:
            return render(request, 'admin.html')

def editProfile(request):
    if request.user.is_authenticated:
        
        count = apiModels.empData.objects.filter(eid=request.user.id).count()
        print(count)
        if count < 1:
            if request.method == "POST":
                form = modelForms.empForm(request.POST, request.FILES)
                print('####')
                if form.is_valid():
                    form.eid = request.user.id
                    data = form.cleaned_data
                    #jsondata = json.dumps(data)

                    print(data)
                    form.save()
                    empListModel = apiModels.empList.objects.create(eid=User.objects.get(pk=request.user.id), date=None)
                    empListModel.save()
                    
                    return HttpResponse('form is valid')
                
                return render(request, "test.html", {
                    "form": form,
                })
        else:
            form1 = modelForms.userInfo()
            form2 = modelForms.empForm(initial={
                'eid':request.user.id,
            })
            return render(request, 'profile_edit.html', {
                'form':form1,
                'form1': form2,
            })
            
        
        form = modelForms.empForm(initial={
            'eid':request.user.id,
        })
    

        return render(
            request,
            "test.html",
            {
                "form": form,
            },
        )



def verifyEmp(request, id):

    empDataModel = apiModels.empData.objects.get(pk=id)

    if request.method == "POST": 
        
        status = request.POST['radio']
        emp = apiModels.empList.objects.get(eid=id)
        if status == "accept":
            empDataModel.status = status
            empDataModel.save()
            emp.date = datetime.date.today()
            emp.status = True
            emp.save()
            messages.add_message(request, messages.INFO, 'Applicatin of ['+str(empDataModel.eid)+'] is Approved')
            return redirect('dash')
        elif status == "reject":
            empDataModel.status = status
            empDataModel.save()
            emp.delete()
            messages.add_message(request, messages.INFO, 'Applicatin of '+str(empDataModel.eid)+' is Rejected')
            return redirect('dash')

        return HttpResponse(request)

    form = modelForms.empForm(initial={
        'eid' : empDataModel.eid,
        'address' : empDataModel.address,
        'tenth_marks' : empDataModel.tenth_marks,
        'tenth_cert'  : empDataModel.tenth_cert,
        'twelth_marks'  : empDataModel.twelth_marks,
        'twelth_cert'  : empDataModel.degree_marks,
        'degree_marks' : empDataModel.degree_marks,
        'degree_cert' : empDataModel.degree_cert,
        'resume' : empDataModel.resume,
        'status' : empDataModel.status,
    })

    return render(request, 'verify.html', {
        'form':form,
    })
    return HttpResponse(form)


def empList(request):
    pass