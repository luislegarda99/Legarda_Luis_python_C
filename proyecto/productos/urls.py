from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.Inicio.as_view(), name="Inicio"),
    path("insertar/", views.insertar_producto, name="insertar")
]