from django.contrib import admin

# Register your models here.
from enfermedades.models import enfermedad
from enfermedades.models import RegistrarEnfermedad

admin.site.register(enfermedad)
admin.site.register(RegistrarEnfermedad)