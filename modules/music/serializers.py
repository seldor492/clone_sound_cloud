from rest_framework import serializers
from .models import Cancion,Album


class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ("id","nombre", "anio", "genero", "album", "rating","url_cancion")

class AlbumSerializer(serializers.ModelSerializer):
    canciones = CancionSerializer(read_only = True, many = True)
    class Meta:
        model = Album
        fields = ("id","nombre", "anio", "rating","genero","autor","canciones")


