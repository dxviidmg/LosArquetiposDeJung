from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^shows', views.ListEventos.as_view(),name="listEventos"),
]