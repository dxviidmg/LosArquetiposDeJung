from django.shortcuts import render
from django.views.generic import View

class Home(View):
	def get(self, request):
		template_name = 'index.html'
		return render(request, template_name)
class Bio(View):
	def get(self, request):
		template_name = 'bio.html'
		return render(request, template_name)
# Create your views here.
