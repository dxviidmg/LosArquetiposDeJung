from django.shortcuts import render
from django.views.generic import View
from .models import Foto

class Galeria(View):
	def get(self, request):
		template_name="galeria/galeria.html"
		fotos = Foto.objects.all()
		context = {
			'fotos': fotos,
		}
		return render(request, template_name, context)
