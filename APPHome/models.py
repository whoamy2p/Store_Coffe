
from django.db import models

# Create your models here.

class Producto (models.Model):
    titulo=models.CharField (max_length=30)
    image=models.ImageField (upload_to="home")
    create=models.DateField (auto_now_add=True)
    update=models.DateField (auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__ (self):
        return self.titulo