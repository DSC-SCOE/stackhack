from django.contrib import admin
from django.urls import path, include
from mainApp import views



urlpatterns = [
    path('signup/', views.signUp, name="signup"),
    path('login/', views.Login, name="login"),
    path('dashboard/', views.dash, name="dash"),
    path('dashboard/', views.dash, name="profile"),
    path('emp/edit/', views.editProfile, name="edit_profile"),
    path('logout/', views.Logout, name='logout')
]


