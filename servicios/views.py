from django.shortcuts import render , redirect
from .models import Eventos,Producto

# Create your views here.

def habitacion (request, tipo=None):
    categorias_disponibles = Producto.objects.values_list('categoria', flat=True).distinct()
    
    if tipo in categorias_disponibles:
        list_productos = Producto.objects.filter(categoria= tipo)
        contexto ={
            "tipo":tipo,
            "list_productos":list_productos
        }
        return render(request,'servicios/habitacion/lista_productos.html',contexto)
    elif tipo == 'carrito':
        return render(request,'servicios/habitacion/carrito.html',context={})
    else:
        return render(request,'servicios/habitacion/carrito.html',context={})
    

# def carrito (request):
#         return render(request,'servicios/habitacion/carrito.html',context={})





def actividades(request):
    model = Eventos
    contexto = {
        "list_eventos": model.objects.all()
    }
    return render (request, 'servicios/actividades.html',contexto)