from django.shortcuts import render
from rest_framework import generics,filters
from .models import Artista
from .serializers import ArtistaSerializer
import django_filters.rest_framework
# Create your views here.

class ListArtista(generics.ListCreateAPIView):
    queryset=Artista.objects.all()
    serializer_class = ArtistaSerializer

    filter_backends =  (filters.SearchFilter,
    django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('id', 'nombre','genero')
    search_fields = ('nombre','genero')


class DetailArtista(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

