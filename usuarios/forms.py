from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class RegistroForm(UserCreationForm):
	class Meta:
		model = Usuario
		fields = ('username', 'email', 'password1', 'password2', 'tipo_usuario')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['tipo_usuario'].initial = 'cliente'

		if not kwargs.get('initial', {}).get('es_admin'):
			self.fields['tipo_usuario'].widget = forms.HiddenInput()

class PerfilForm(UserChangeForm):
	password = None

	class Meta:
		model = Usuario
		fields = ('first_name', 'last_name', 'email', 'telefono', 'avatar',
				  'dni', 'fecha_nacimiento', 'nombre_empresa', 'cif')
