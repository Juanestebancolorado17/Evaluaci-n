from django.contrib import admin
from .models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    readonly_files = ('created', 'updated')

admin.site.register(Alumno)
    

