from django.forms import ModelForm
from .models import *

class JugadorForm(ModelForm):
  class Meta:
    model = Jugadores
    fields = '__all__'

class EquipoForm(ModelForm):
  class Meta:
    model = Equipos
    fields = '__all__'

class EstadioForm(ModelForm):
  class Meta:
    model = Estadios
    fields = '__all__'