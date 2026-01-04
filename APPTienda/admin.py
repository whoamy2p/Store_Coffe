from django.contrib import admin
from APPTienda.models import Grano, Tostado, Molido, Producto

# Register your models here.

class ProductoAdmin (admin.ModelAdmin):
    list_display = ("titulo", "contenido", "imagen", "precio", "stock", "peso", "destacado", "origen", "productor", "altura", "molidos", "create", "update")
    list_editable = ("contenido", "productor")
    list_filter = ("titulo", "precio", "stock", "peso", "destacado", "origen", "molidos", "granos", "tostados", "create", "update")
    date_hierarchy = "create"
    readonly_fields = ("create", "update")
    search_fields = ("titulo", "origen", "molidos", "granos", "tostados")

class GranoAdmin (admin.ModelAdmin):
    list_display = ("categoria_grano", "create", "update")
    list_filter = ("categoria_grano",)
    search_fields = ("categoria_grano",)
    date_hierarchy = "create"
    readonly_fields = ("create", "update")

class TostadoAdmin (admin.ModelAdmin):
    list_display = ("categoria_tostado", "create", "update")
    list_filter = ("categoria_tostado",)
    search_fields = ("categoria_tostado",)
    date_hierarchy = "create"
    readonly_fields = ("create", "update")

class MolidoAdmin (admin.ModelAdmin):
    list_display = ("categoria_molido", "create", "update")
    list_filter = ("categoria_molido",)
    search_fields = ("categoria_molido",)
    date_hierarchy = "create"
    readonly_fields = ("create", "update")

admin.site.register (Producto, ProductoAdmin)
admin.site.register (Grano, GranoAdmin)
admin.site.register (Tostado, TostadoAdmin)
admin.site.register (Molido, MolidoAdmin)
