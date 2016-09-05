from django.db import models

class Integrante(models.Model):
	nombre = models.CharField(max_length=10)
	rol = models.CharField(max_length=20)
	foto = models.FileField(upload_to='integrante/%Y/%m/%d/', null=True, blank=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['id']