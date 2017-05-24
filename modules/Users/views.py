from django.shortcuts import render
from rest_framework import generics,filters
from .models import User
from .serializers import UserSerializer
import django_filters.rest_framework
# Create your views here.

class ListUser(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

    filter_backends =  (filters.SearchFilter,
    django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('biblioteca',)
    search_fields = ('nombre','apellidos')


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer