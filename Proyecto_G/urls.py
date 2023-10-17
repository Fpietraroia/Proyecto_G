from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect

def redireccion_inicio(request):
    return redirect('/GymApp/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('GymApp/', include('GymApp.urls')),
    path('', redireccion_inicio, name='redireccion-inicio'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)