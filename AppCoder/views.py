from django.shortcuts import render

from AppCoder.models import Estudiante

def mostrar_inicio(request):
    estudiante = Estudiante(nombre = 'Cesar', email = 'cesar@appcoder.com ')
    contexto = {'estudiante_1' : estudiante}
    estudiante.save()    
    return render(request, "AppCoder/inicio.html", contexto)