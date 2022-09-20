from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('equipos/', views.equipos, name="equipos"),
    path('jugadores/', views.jugadores, name="jugadores"),
    path('estadios/', views.estadios, name="estadios"),

    path('create_jugador/', views.createJugador, name="create_jugador"),
    path('create_equipo/', views.createEquipo, name="create_equipo"),
    path('create_estadio/', views.createEstadio, name="create_estadio"),

    path('update_jugador/<int:pk>/', views.updateJugador, name="update_jugador"),
    path('update_estadio/<int:pk>/', views.updateEstadio, name="update_estadio"),
    path('update_equipo/<int:pk>/', views.updateEquipo, name="update_equipo"),

    path('delete_estadio/<int:pk>', views.deleteEstadio, name="delete_estadio"),
    path('delete_equipo/<int:pk>', views.deleteEquipo, name="delete_equipo"),
    path('delete_jugador/<int:pk>', views.deleteJugador, name="delete_jugador"),
]