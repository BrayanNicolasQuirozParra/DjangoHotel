from django.shortcuts import render, redirect
from hotelhe.models import Habitacion, Turismo
# Create your views here.

def list(request):
    return render(request, "inicio/index.html")

def list(request):
    return render(request, "inicio/index.html")

def list_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, "inicio/habitaciones.html", {"habitaciones" : habitaciones})


def list_turismo(request):
    turismo = Turismo.objects.all()
    return render(request, "inicio/turismolist.html", {"turismo": turismo})


def habitaciones(request):
    if request.method == "GET":
        return render(request,"inicio/habitaciones.html")

    nombrePersona = request.POST["nombrepersona_habitaciones"]
    telefono = request.POST["telefono_habitaciones"]
    numeroPersonas = request.POST["npersonas_habitaciones"]
    tipo = request.POST["tipo_habitaciones"]
    dias = request.POST["dias_habitaciones"]

    guardar_habitaciones = Habitacion(nombrePersona=nombrePersona, telefono=telefono, numeroPersonas=numeroPersonas, tipo=tipo, dias=dias)
    guardar_habitaciones.save()

    return redirect('inicio:list_inicio')

def turismo(request):
    if request.method == "GET":
        return render(request,"inicio/turismocrear.html")
    imagen = request.FILES["imagen_turismo"]
    nombre = request.POST["nombre_turismo"]
    hora = request.POST["hora_turismo"]
    precio = request.POST["precio_turismo"]
    descripcion = request.POST["descripcion_turismo"]


    guardar_turismo = Turismo(imagen=imagen, nombre=nombre, hora=hora, precio=precio ,descripcion=descripcion)
    guardar_turismo.save()

    return redirect('inicio:list_turismo')