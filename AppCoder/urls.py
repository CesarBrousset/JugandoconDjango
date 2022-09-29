from django.urls import path

from AppCoder.views import mostrar_inicio

urlpatterns = [
    path("inicio/", mostrar_inicio)
]