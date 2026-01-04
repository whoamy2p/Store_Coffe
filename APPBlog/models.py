
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria (models.Model):
    nombre = models.CharField (max_length=30)
    
    create = models.DateField (auto_now_add=True)
    update = models.DateField (auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__ (self):
        return self.nombre

class Post (models.Model):
    titulo = models.CharField (max_length=30)
    contenido = models.CharField (max_length=150)
    imagen = models.ImageField (upload_to="blog")
    autor = models.ForeignKey (User, on_delete=CASCADE)
    catagoria = models.ManyToManyField (Categoria)

    create = models.DateField (auto_now_add=True)
    update = models.DateField (auto_now_add=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__ (self):
        return self.titulo
