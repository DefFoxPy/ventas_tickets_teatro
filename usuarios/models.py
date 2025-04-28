from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
	TIPOS_USUARIO = (
		('admin', 'Adiministrador'),
		('organizador', 'Organizador de Eventos'),
		('cliente', 'Cliente'),
	)

	tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='cliente')
	telefono = models.CharField(max_length=20, blank=True)
	avatar = models.ImageField(upload_to='usuarios/avatars/', blank=True)

	# Campos adicionales para clientes
	dni = models.CharField(max_length=20, blank=True, verbose_name="Cédula")
	fecha_nacimiento = models.DateField(null=True, blank=True)

	# Campos para organizadores
	nombre_empresa = models.CharField(max_length=100, blank=True)
	cif = models.CharField(max_length=20, blank=True, verbose_name="CIF")

	#verificación
	email_verificado = models.BooleanField(default=False)

	class Meta:
		verbose_name = _('usuario')
		verbose_name_plural = _('usuarios')

	def __str__(self):
		return self.get_full_name() or self.username

	@property
	def es_organizador(self):
		return self.tipo_usuario == 'organizador'

	@property
	def puede_crear_eventos(self):
		return self.es_organizador or self.is_staff
