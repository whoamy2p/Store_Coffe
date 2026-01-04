from django.shortcuts import render
from APPHome.models import Producto

# Create your views here.

def home (request):
    product_data=Producto.objects.all ()

    return render (request, "APPHome/home.html", {"data": product_data})

def quienes_somos (request):
    product_data=Producto.objects.all ()

    return render (request, "APPHome/sobre_nosotros.html", {"data": product_data})