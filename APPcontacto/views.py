
from django.shortcuts import redirect, render
from APPcontacto.forms import Formulario
from django.core.mail import EmailMessage

# Create your views here.

def contactanos (request):
    form=Formulario ()

    if request.method == "POST":
        my_form=Formulario (data=request.POST)

        if my_form.is_valid ():
            name=request.POST.get ('nombre')
            email=request.POST.get ("correo")
            messenger=request.POST.get ("mensaje")

            email=EmailMessage ("Información de producto", f"El usuario {name} envio un mensaje\n\n {messenger}", "", ["fioces0608@gmail.com"], reply_to=[email])

            try:
                email.send ()
                return redirect ("/Contacto/?valido")
            except:
                return redirect ("/Contacto/?novalido")

    return render (request, "APPContacto/contacto.html", {"Forms":form})
