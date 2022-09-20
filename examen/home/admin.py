from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Equipos)
admin.site.register(Estadios)
admin.site.register(Jugadores)