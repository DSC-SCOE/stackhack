from django.shortcuts import render
from .forms import signupForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import generics

from .serializers import UserSerializer, EmployeeSerializer, EmployeeDataSerializer
from .models import empModel, empData

import io
import json


def test(request):
    form = signupForm()
    return render(request, "test.html", {"form": form})


@csrf_exempt
def addUser(request):
    if request.method == "POST":
        jsondata = request.body
        print("###")
        stream = io.BytesIO(jsondata)
        print(stream)
        pydata = JSONParser().parse(stream)

        serializer = UserSerializer(data=pydata)
        print(serializer.error_messages)

        if serializer.is_valid():
            print(pydata)
            serializer.save()
            res = "user created"
            #jsondata = JSONRenderer().render(res)
            return HttpResponse(res)
            return JsonResponse(jsondata, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)


class Employee_all(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = empData.objects.all()


class Employee_specific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = empModel.objects.all()


class EmployeeData_all(generics.ListCreateAPIView):
    serializer_class = EmployeeDataSerializer
    queryset = empData.objects.all()


class EmployeeData_specific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDataSerializer
    queryset = empData.objects.all()