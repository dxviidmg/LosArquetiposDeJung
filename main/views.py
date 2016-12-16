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
		banda = Banda.objects.get(pk=1)
		context = {
			'banda': banda
		}
		return render(request, template_name, context)