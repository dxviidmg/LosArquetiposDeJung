from django.shortcuts import render
from django.views.generic import View
from .models import Banda

class Home(View):
	def get(self, request):
		template_name = 'main/home.html'
		return render(request, template_name)
class Bio(View):
	def get(self, request):
		template_name = 'main/bio.html'
		bandas = Banda.objects.all()
		context = {
			'bandas': bandas
		}
		return render(request, template_name, context)