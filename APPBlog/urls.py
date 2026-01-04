from typing import ValuesView
from django.urls import path
from APPBlog import views

urlpatterns = [
    path ("", views.blog_post, name="Blog"),
    path ("categoria/<int:categoria_id>/", views.categorias_post, name="Categoria"),
]