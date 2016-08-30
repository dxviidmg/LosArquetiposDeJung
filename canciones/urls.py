from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^canciones', views.ListCanciones.as_view(),name="listCanciones"),
	url(r'^(?P<slug>[-\w]+)/$', views.LetraCancion.as_view(), name="letraCancion"),
]