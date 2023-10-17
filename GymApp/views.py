from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from GymApp.models import *
from GymApp.forms import *
from django.contrib.auth.decorators import login_required

# Vista de inicio

def inicio (request):
    return render(request, "GymApp/inicio.html")

#-----------------------------------------------------------------------------------------