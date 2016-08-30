from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^integrantes', views.ListIntegrantes.as_view(),name="listIntegrantes"),
]