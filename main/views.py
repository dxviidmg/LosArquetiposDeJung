from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Banda

class Home(View):
	def get(self, request):
		template_name = 'main/home.html'
		return render(request, template_name)
class Bio(View):
	def get(self, request):
		template_name = 'main/bio.html'
		banda = get_object_or_404(Banda, pk=1)
		print(banda)
		context = {
			'banda': banda
		}
		return render(request, template_name, context)