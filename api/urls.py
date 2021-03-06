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
    path("employee/data/", views.EmployeeData_all.as_view(), name="employeeData_all"),
    path(
        "employee/data/<int:pk>/",
        views.EmployeeData_specific.as_view(),
        name="employeeData_specific",
    ),
    path("employee/leave/", views.Leave_all.as_view(), name="leave_all"),
    path(
        "employee/leave/<int:pk>/",
        views.Leave_specific.as_view(),
        name="leave_specific",
    ),
]
