from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^eventos', views.ListEventos.as_view(),name="listEventos"),
]