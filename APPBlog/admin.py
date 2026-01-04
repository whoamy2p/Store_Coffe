from django.contrib import admin
from APPBlog.models import Categoria, Post

# Register your models here.

class CategoriaAdmin (admin.ModelAdmin):
    search_fields = ("nombre",)
    list_display = ("nombre", "create", "update")
    list_filter = ("nombre", "create")
    readonly_fields = ("create", "update")
    date_hierarchy = "create"

class PostAdmin (admin.ModelAdmin):
    search_fields = ("titulo", "categoria")
    list_display = ("titulo", "contenido", "imagen", "autor", "create", "update")
    list_filter = ("titulo", "autor")
    date_hierarchy = "create"
    list_editable = ("contenido",)
    readonly_fields = ("create", "update")

admin.site.register (Categoria, CategoriaAdmin)
admin.site.register (Post, PostAdmin)
