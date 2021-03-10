from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('login', views.login_attempt, name="login_attempt"),
    path('register', views.register_attempt, name="register_attempt"),
    path('logout', views.logout_attempt, name="logout_attempt"),
]