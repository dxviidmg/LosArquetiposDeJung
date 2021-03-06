from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Cancion

class ListCanciones(View):
	def get(self, request,):
		template_name = "canciones/canciones.html"
		canciones = Cancion.objects.all().order_by("titulo")
		context = {
		'canciones': canciones
		}
		return render(request, template_name, context)

class LetraCancion(View):
	def get(self, request, slug):
		template_name = "canciones/letra.html"
		cancion = get_object_or_404(Cancion,slug=slug)
		context = {
		'cancion': cancion
		}
		return render(request, template_name, context)