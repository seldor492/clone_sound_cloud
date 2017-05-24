from django.shortcuts import render
from rest_framework import generics, filters, status
from .models import Album, Cancion
from .serializers import AlbumSerializer,CancionSerializer
import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser,MultiPartParser
from django.conf import settings

# Create your views here.

class ListAlbum(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    #filter_backends = (filter)    
    filter_backends =  (filters.SearchFilter,
    django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('nombre','anio','autor','genero')
    search_fields = ('nombre','genero')


class DetailAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ListCanciones(generics.ListCreateAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
    #filters
    filter_backends =  (filters.SearchFilter,
    django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('nombre','anio','album','genero')
    search_fields = ('nombre','genero')



class DetailCanciones(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

class UploadFiles(APIView):
    
    parser_classes = (FormParser,MultiPartParser)
    def handle_uploaded_file(self,f):
        print(settings.MEDIA_ROOT)
        path = "%s/%s" % (settings.MEDIA_ROOT,str(f))
        print(path)
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def post(self,request):
        
        try:
            print(request.FILES['file'])
            self.handle_uploaded_file(request.FILES['file'])
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(status=status.HTTP_200_OK)
