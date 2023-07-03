from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Productos
from .forms import ProductoForm
from django.views import View


# Create your views here.
def index(request):
    
    return HttpResponse("Url creado correctamente")
    
class Inicio(View):
    template_name = "index.html"
    
    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio/')
        
        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        productos = Productos.objects.all()
        form = ProductoForm()
        
        return render(request, self.template_name, {'form': form, "productos": productos})
    
    
def insertar_producto(request):
    nuevo_producto = Productos(
        nombre = "PS4",
        descripcion = "consola de videojuegos",
        precio = 10000,
        fecha_registro ="2023-12-06", 
        estatus = True,
    )
    nuevo_producto.save()
    
    
    return HttpResponse("Producto agregado correctamente")
    