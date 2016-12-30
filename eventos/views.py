from django.shortcuts import render
from django.views.generic import View
from .models import Evento
from datetime import date

class ListEventos(View):
	def get(self, request):
		template_name="eventos/eventos.html"
		hoy = date.today()
		eventos = Evento.objects.all().order_by("fecha")
		eventosf = []
		for evento in eventos:
			if evento.fecha >= hoy:
				eventosf.append(evento)
		context={'eventosf':eventosf}
		return render(request, template_name, context)
# Create your views here.


