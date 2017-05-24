from rest_framework import serializers
from modules.music.serializers import AlbumSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'nombre', 'apellidos', 'biblioteca','albums')