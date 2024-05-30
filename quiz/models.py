from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    numero_ficha = models.CharField(max_length=20)
    email = models.EmailField()
    upgrated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

    def __str__(self):
        return self.nombre
    
