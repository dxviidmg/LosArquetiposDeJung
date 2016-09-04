from django.db import models

#Libreria para la generacion de urls
from django.core.urlresolvers import reverse


class Cancion(models.Model):
	titulo = models.CharField(max_length=30)
	letra = models.TextField()
	slug = models.SlugField()

	def __str__(self):
		return self.titulo
			#Genera url con un dato de la BD del modelo
	def get_absolute_url(self):
		return reverse('canciones:letraCancion', args=[self.slug])