from django.shortcuts import render
from .forms import signupForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import generics

from .serializers import UserSerializer, EmployeeSerializer
from .models import empModel

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
            res = {"msg": "user created"}
            jsondata = JSONRenderer().render(res)
            return JsonResponse(jsondata, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)


class Employee_all(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = empModel.objects.all()


class Employee_specific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = empModel.objects.all()