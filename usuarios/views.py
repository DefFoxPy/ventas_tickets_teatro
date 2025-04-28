from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import RegistroForm, PerfilForm
from .models import Usuario

def registro(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			#return redirect('eventos:lista')
	else:
		form = RegistroForm()

	return render(request, 'registro.html', {'form': form})

@login_required
def perfil(request):
	return render(request, 'perfil.html')

class ActualizarPerfil(UpdateView):
	model = Usuario
	form_class = PerfilForm
	template_name = 'editar_perfil.html'
	success_url = reverse_lazy('usuarios:perfil')

	def get_object(self):
		return self.request.user
