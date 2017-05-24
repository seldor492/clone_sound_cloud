from rest_framework import serializers
from modules.music.serializers import AlbumSerializer
from .models import Artista


class ArtistaSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(read_only=True,many=True)
    class Meta:
        model = Artista
        fields = ('id', 'nombre', 'nacionalidad', 'acerca_de','tipo_artista','genero','albums')


