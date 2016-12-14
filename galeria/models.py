from django.db import models
from django.utils import timezone

class Foto(models.Model):
	imagen = models.ImageField(upload_to='galeria/%Y/%m/%d/')
	descripcion = models.TextField(max_length=50)
	creacion = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['pk']
	
	def __str__(self):
		return '{} {}'.format(self.descripcion, self.creacion)