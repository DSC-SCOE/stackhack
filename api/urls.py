from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("test/", views.test),
    path("user/", views.addUser, name="addUser"),
    path("employee/", views.Employee_all.as_view(), name="employee_all"),
    path(
        "employee/<int:pk>/",
        views.Employee_specific.as_view(),
        name="employee_specific",
    ),
]
