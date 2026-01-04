from django import forms

class Formulario (forms.Form):
    nombre=forms.CharField (required=True, max_length=35, widget=forms.TextInput (attrs={"placeholder":"Ingrese su nombre"}))
    correo=forms.EmailField (required=True, max_length=50, widget=forms.TextInput (attrs={"placeholder":"Correo electronico", "size":20}))
    mensaje=forms.CharField (required=True, widget=forms.Textarea (attrs={'cols': 50, 'rows': 12, "placeholder":"Escriba aquí su mensaje"}))