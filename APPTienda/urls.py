from django.urls import path
from APPTienda import views

urlpatterns = [
    path ("", views.tienda, name="Tienda"),
    path("Category/", views.categoria_tienda, name="Categoria_tienda")
]