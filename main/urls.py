from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(),name="home"),
	url(r'^biografia', views.Bio.as_view(),name="bio"),
]