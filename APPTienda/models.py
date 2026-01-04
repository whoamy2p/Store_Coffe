
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Grano (models.Model):
    categoria_grano = models.CharField (max_length=250)
    create = models.DateField (auto_now_add=True)
    update = models.DateField (auto_now_add=True)
    # verde, seco

    class Meta:
        ordering = ["categoria_grano"]
        verbose_name = "Grano"
        verbose_name_plural = "Granos"

    def __str__ (self):
        return self.categoria_grano


class Tostado (models.Model):
    categoria_tostado = models.CharField (max_length=250)
    create = models.DateField (auto_now_add=True)
    update = models.DateField (auto_now_add=True)
    # claro, medio, oscuro

    class Meta:
        ordering = ["categoria_tostado"]
        verbose_name = "Tostado"
        verbose_name_plural = "Tostados"

    def __str__ (self):
        return self.categoria_tostado

class Molido (models.Model):
    categoria_molido = models.CharField (max_length=250)
    create = models.DateField (auto_now_add=True)
    update = models.DateField (auto_now_add=True)
    # fino, grueso, medio

    class Meta:
        verbose_name = "Molido"
        verbose_name_plural = "Molidos"

    def __str__ (self):
        return self.categoria_molido


class Producto (models.Model):
    titulo = models.CharField (max_length=50)
    contenido = models.CharField (max_length=300)
    imagen = models.ImageField (upload_to="tienda")
    precio = models.FloatField ()

    stock = models.BooleanField ()
    peso = models.FloatField ()
    destacado = models.BooleanField ()
    origen = models.CharField (max_length=30, blank=True, null=True)
    productor = models.CharField (max_length=50, blank=True, null=True)
    altura = models.IntegerField (blank=True, null=True)

    molidos = models.ForeignKey (Molido, on_delete=CASCADE, blank=True, null=True) # presentacion
    granos = models.ManyToManyField (Grano) # presentacion
    tostados = models.ManyToManyField (Tostado)

    create = models.DateField (auto_now_add=True)
    update = models.DateField (auto_now_add=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__ (self):
        return self.titulo
