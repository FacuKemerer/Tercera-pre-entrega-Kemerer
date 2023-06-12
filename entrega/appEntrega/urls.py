"""
URL configuration for projecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    inicio,
    horarios,
    servicio,
    agregar_cliente,
    agregar_auto,
    agregar_historia,
    busqueda_auto,
)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('horarios/', horarios, name="Horarios"),
    path('servicio/', servicio, name="Servicio"),
    path('form_hist/', agregar_historia, name="AgregarHistorial"),
    path('form_cliente/', agregar_cliente, name="AgregarCliente"),
    path('form_auto/', agregar_auto, name="AgregarAuto"),
    path('busqueda/', busqueda_auto, name="Busqueda"),
]
