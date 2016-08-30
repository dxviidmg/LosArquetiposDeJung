from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    lugar = models.CharField(max_length=50)
    flyer = models.FileField(upload_to='evento/%Y/%m/%d/', null=True, blank=True)

    class Meta:
    	ordering = ['-fecha']

    def __str__(self):
    	return self.nombre
# Create your models here.
