from django.db import models

# Create your models here.

class Artista(models.Model):
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

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    acerca_de = models.TextField()
    tipo_artista = models.CharField(choices=(('G','Grupo'),('S','Solista')), max_length=50)
    genero = models.CharField(choices=GENEROS,max_length=100)

    def __str__(self):
        return "Artista: %s" % (self.nombre,)
