from django.contrib import admin
from .models import Artista

class ArtistaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Artista, ArtistaAdmin)

# Register your models here.
# Register your models here.
