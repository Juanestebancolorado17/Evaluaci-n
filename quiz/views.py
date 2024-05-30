from django.shortcuts import render
from .models import Alumno

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'quiz.html', {'alumnos': alumnos})


