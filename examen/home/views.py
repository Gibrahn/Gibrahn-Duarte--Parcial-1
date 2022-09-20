from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.
def home(request):
  equipos = Equipos.objects.all()
  jugadores = Jugadores.objects.all()
  estadios = Estadios.objects.all()

  context = {'equipos':equipos, 'jugadores':jugadores, 'estadios':estadios}

  return render (request, 'home/dashboard.html', context)

def equipos(request):
  return render (request, 'home/equipos.html')

def jugadores(request):
  return render (request, 'home/jugadores.html')

def estadios(request):
  return render (request, 'home/estadios.html')

def createJugador(request):
  form = JugadorForm
  if request.method == 'POST':
    #print('Printing POST:', request.POST)
    form = JugadorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')

  context = {'form': form}
  return render(request, 'home/jugadores_form.html', context)

def createEstadio(request):
  form = EstadioForm
  if request.method == 'POST':
    #print('Printing POST:', request.POST)
    form = EstadioForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')

  context = {'form': form}

  return render(request, 'home/estadios_form.html', context)

def createEquipo(request):
  form = EquipoForm
  if request.method == 'POST':
    #print('Printing POST:', request.POST)
    form = EquipoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')

  context = {'form':form}
  return render(request, 'home/equipos_form.html', context)



def deleteEquipo(request, pk):
  equipo = Equipos.objects.get(pk=pk)
  equipo.delete()
  return redirect('/')

def deleteJugador(request, pk):
  jugador = Jugadores.objects.get(pk=pk)
  jugador.delete()
  return redirect('/')

def deleteEstadio(request, pk):
  estadio = Estadios.objects.get(pk=pk)
  estadio.delete()
  return redirect('/')

def updateJugador(request, pk):
  
	jugador = Jugadores.objects.get(pk=pk)
	form = JugadorForm(instance=jugador)

	if request.method == 'POST':
		form = JugadorForm(request.POST, instance=jugador)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'home/jugadores_form.html', context)

def updateEstadio(request, pk):
  
	estadio = Estadios.objects.get(pk=pk)
	form = EstadioForm(instance=estadio)

	if request.method == 'POST':
		form = EstadioForm(request.POST, instance=estadio)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'home/estadios_form.html', context)

def updateJugador(request, pk):
  
	jugador = Jugadores.objects.get(pk=pk)
	form = JugadorForm(instance=jugador)

	if request.method == 'POST':
		form = JugadorForm(request.POST, instance=jugador)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'home/jugadores_form.html', context)

def updateEquipo(request, pk):
  
	equipo = Equipos.objects.get(pk=pk)
	form = EquipoForm(instance=equipo)

	if request.method == 'POST':
		form = EquipoForm(request.POST, instance=equipo)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'home/equipos_form.html', context)