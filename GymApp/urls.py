from django.urls import path
from GymApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),


    ]

