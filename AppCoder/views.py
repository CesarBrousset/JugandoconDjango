from django.template import Context, Template

from django.http import HttpResponse

import random
import datetime

def saludo(request):
    return HttpResponse('Buenas noches!')

def saludo_con_nombre(request, nombre, edad):
    hoy = datetime.datetime.now()
    return HttpResponse(f'Buenas noches!: {nombre} <br> tu edad es {edad}')

def saludo_con_template(request):
    mi_archivo = open(r'C:\ProyectoCoder\MVTCesarBrousset\AppCoder\templates\template1.html')
    template = Template(mi_archivo.read())
    mi_archivo.close()
    
    context = Context()
    
    res = template.render(context)
    return HttpResponse(res)