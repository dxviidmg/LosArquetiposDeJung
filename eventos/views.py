from django.shortcuts import render
from django.views.generic import View
from .models import Evento

class ListEventos(View):
	def get(self, request):
		template_name="eventos.html"
		eventos = Evento.objects.all().order_by('fecha')
		context = {
		'eventos': eventos
		}
		return render(request, template_name, context)
# Create your views here.
