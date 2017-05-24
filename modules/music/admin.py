from django.contrib import admin
from .models import Cancion, Album

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    pass

class CancionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Album,AlbumAdmin)
admin.site.register(Cancion,CancionAdmin)