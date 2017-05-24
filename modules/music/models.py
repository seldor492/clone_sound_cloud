from django.db import models
from modules.Artistas.models import Artista

# Create your models here.
GENEROS = (
        ("LA","Latina"),
        ("PO","Pop"),
        ("RO","Rock"),
        ("IA","Indie/Alternativa"),
        ("DA","Dance"),
        ("HH","Hip Hop"),
        ("RB","Rhythm and Blues"),
        ("CO","Country"),
        ("FA","Folk & Americana"),
        ("ME", "Metal"),
        ("SO", "Soul"),
        ("JA", "Jazz"),
        ("BL", "Blues"),
        ("PU", "Punk"),
        ("FU", "Funk"),
        ("CL", "Clásica"),

    )

class Album(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    anio = models.IntegerField()
    rating = models.DecimalField(max_digits = 3, decimal_places=2, default=0.00, blank=True,null=True)
    autor = models.ForeignKey(Artista,
        on_delete = models.CASCADE, null=True, blank=True, related_name="albums")
    genero = models.CharField(choices = GENEROS, max_length = 20)

    def __str__(self):
        return "Album: %s" % (self.nombre,)


class Cancion(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    anio = models.IntegerField()
    rating = models.DecimalField(max_digits = 3, decimal_places=2, default=0.00, blank=True,null=True)
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = "canciones")
    genero = models.CharField(choices = GENEROS, max_length = 20)
    url_cancion = models.CharField(max_length = 200, blank=True,null=True)

    def __str__(self):
        return "Cancion: %s" % (self.nombre,)