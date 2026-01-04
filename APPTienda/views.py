from django.shortcuts import render
from APPTienda.models import Producto, Grano, Molido, Tostado
from django.db.models import Q

# Create your views here.

def tienda (request):
    # Obtener todos los productos
    productos = Producto.objects.all()
    
    # Búsqueda
    buscar = request.GET.get('buscar', '')
    if buscar:
        productos = productos.filter(
            Q(titulo__icontains=buscar) | 
            Q(contenido__icontains=buscar) |
            Q(origen__icontains=buscar)
        )
    
    # Filtro por precio
    precio_min = request.GET.get('precio_min', '')
    precio_max = request.GET.get('precio_max', '')
    
    if precio_min:
        try:
            productos = productos.filter(precio__gte=float(precio_min))
        except ValueError:
            pass
    
    if precio_max:
        try:
            productos = productos.filter(precio__lte=float(precio_max))
        except ValueError:
            pass
    
    # Filtro por tipo de grano/molido
    filtro_grano = request.GET.get('grano', '')
    if filtro_grano:
        if filtro_grano == 'Tostado':
            productos = productos.filter(granos__categoria_grano__icontains='Tostado')
        elif filtro_grano in ['Fino', 'Medio', 'Grueso', 'Extra Fino']:
            productos = productos.filter(molidos__categoria_molido__icontains=filtro_grano)
    
    # Obtener rango de precios para el slider
    todos_productos = Producto.objects.all()
    precio_minimo = todos_productos.order_by('precio').first().precio if todos_productos.exists() else 0
    precio_maximo = todos_productos.order_by('-precio').first().precio if todos_productos.exists() else 100
    
    # Obtener opciones de filtro con conteos
    opciones_grano = []
    
    # Grano Tostado
    tostado_count = Producto.objects.filter(granos__categoria_grano__icontains="Tostado").distinct().count()
    if tostado_count > 0:
        opciones_grano.append({
            'nombre': 'Grano Tostado',
            'valor': 'Tostado',
            'count': tostado_count
        })
    
    # Tipos de molido
    molidos = Molido.objects.all()
    for molido in molidos:
        count = Producto.objects.filter(molidos=molido).count()
        if count > 0:
            opciones_grano.append({
                'nombre': f'Molido {molido.categoria_molido}',
                'valor': molido.categoria_molido,
                'count': count
            })
    
    return render(request, "APPTienda/productos.html", {
        "data_products": productos.distinct(),
        "opciones_filtro": opciones_grano,
        "buscar_actual": buscar,
        "filtro_actual": filtro_grano,
        "precio_min_actual": precio_min,
        "precio_max_actual": precio_max,
        "precio_minimo": int(precio_minimo),
        "precio_maximo": int(precio_maximo)
    })


def categoria_tienda (request):
    return render (request, "APPTienda/categoria.html")