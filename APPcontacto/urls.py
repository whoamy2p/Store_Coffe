from django.urls import path
from APPcontacto import views

urlpatterns = [
    path ("", views.contactanos, name="Contacto"),
]