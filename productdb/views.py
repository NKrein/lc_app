from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, "index.html")


def formulario_consulta(request):
    return render(request, "formulario_consulta.html")


def consultar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["nikokrein@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "consulta_exitosa.html")
    return render(request, "formulario_consulta.html")