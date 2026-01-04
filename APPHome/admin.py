from django.contrib import admin
from APPHome.models import Producto

# Register your models here.

class ProductoAdmin (admin.ModelAdmin):
    list_display_links = ("image",)
    list_display=("titulo", "image", "create", "update")
    list_filter=("titulo",)
    date_hierarchy="create"
    readonly_fields=("create", "update")
    search_fields=("titulo",)

admin.site.register (Producto, ProductoAdmin)
