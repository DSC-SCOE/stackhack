from django.shortcuts import render
from .forms import signupForm
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import (
    UserSerializer,
    EmployeeSerializer,
    EmployeeDataSerializer,
    LeaveSerializer,
)
from .models import empModel, empData, leaveModel

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
            # jsondata = JSONRenderer().render(res)
            return HttpResponse(res)
            return JsonResponse(jsondata, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)


class Employee_all(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = empModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(eid=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        return queryset.filter(eid=user)


class Employee_specific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = empModel.objects.all()

    def get_permissions(self):
        if self.request.method == "PUT" or self.request.method == "PATCH":
            return [IsAdminUser()]
        else:
            return [IsAuthenticated()]


class EmployeeData_all(generics.ListCreateAPIView):
    serializer_class = EmployeeDataSerializer
    queryset = empData.objects.all()

    def perform_create(self, serializer):
        serializer.save(eid=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        return queryset.filter(eid=user)


class EmployeeData_specific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDataSerializer
    queryset = empData.objects.all()


class Leave_all(generics.ListCreateAPIView):
    serializer_class = LeaveSerializer
    queryset = leaveModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(eid=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        if user.is_staff:
            return queryset.filter()
        else:
            return queryset.filter(eid=user)


class Leave_specific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeaveSerializer
    queryset = leaveModel.objects.all()
