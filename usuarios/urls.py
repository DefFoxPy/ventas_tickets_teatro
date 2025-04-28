from django.urls import path
from .views import registro, perfil, ActualizarPerfil

app_name = 'usuarios'

urlpatterns = [
	path('registro/', registro, name='registro'),
	path('perfil/', perfil, name='perfil'),
	path('perfil/editar/', ActualizarPerfil.as_view(), name='editar_perfil'),
]