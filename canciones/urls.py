from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^letras/(?P<slug>[-\w]+)/$', views.LetraCancion.as_view(), name="letraCancion"),
	url(r'^letras', views.ListCanciones.as_view(),name="listCanciones"),
	
]