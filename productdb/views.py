from django.shortcuts import render

# Create your views here.


def formulario_consulta(request):
    return render(request, "formulario_consulta.html")