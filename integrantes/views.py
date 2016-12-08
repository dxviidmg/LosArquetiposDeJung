from django.shortcuts import render
from django.views.generic import View
from .models import Integrante

class ListIntegrantes(View):
	def get(self, request):
		template_name="integrantes/integrantes.html"
		integrantes = Integrante.objects.all()
		context = {
		'integrantes': integrantes
		}
		return render(request, template_name, context)