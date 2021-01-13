from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
     path('test/', views.test),
     path('addEmp/', views.addEmployee, name='addUser'),
]
