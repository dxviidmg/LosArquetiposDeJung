from django.contrib import admin
from .models import Cancion

class CancionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(Cancion, CancionAdmin)
# Register your models here.
