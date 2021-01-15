from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("test/", views.test),
    path("/", views.addUser, name="addUser"),
    path("employee/", views.Employee.as_view(), name="employee"),
]
