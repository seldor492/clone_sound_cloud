from django.shortcuts import render,redirect
import requests
import json
from .forms import AddArtistaForm, AddAlbumForm
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def dashboard(request):
    return render(request, "landing/dashboard.html")


def artistas(request, id=False):
    if request.method == 'POST':
        p = {'search':request.POST['q']}
        r = requests.get("https://cscloud.herokuapp.com/api/v1/artistas",params=p)
        string = r.text
        json_str = json.loads(string, encoding=None)
    else:
        if id:
            data = {
                'id':id,
            }
            r = requests.get("https://cscloud.herokuapp.com/api/v1/artistas", params=data)
            string = r.text
            json_str = json.loads(string, encoding=None)
        else:
            print(request)
            r = requests.get("https://cscloud.herokuapp.com/api/v1/artistas")
            string = r.text
            json_str = json.loads(string, encoding=None)   

    return render(request, "landing/artistas.html", {
        'artistas' : json_str,
        })


def albums(request, artista=False):
    if request.method == 'POST':
        p = {'search':request.POST['q']}
        r = requests.get("https://cscloud.herokuapp.com/api/v1/music/albums",params=p)
        string = r.text
        json_str = json.loads(string, encoding=None)
    else:
        if artista:
            data = {
                'autor':artista
            }
            r = requests.get("https://cscloud.herokuapp.com/api/v1/music/albums", params=data)
            string = r.text
            json_str = json.loads(string, encoding=None)        
        else:
            r = requests.get("https://cscloud.herokuapp.com/api/v1/music/albums")
            string = r.text
            json_str = json.loads(string, encoding=None)

    return render(request, "landing/albums.html", {
        'albums' : json_str,
        })

def canciones(request, album=False):
    if request.method == 'POST':
        p = {'search':request.POST['q']}
        r = requests.get("https://cscloud.herokuapp.com/api/v1/music/canciones/",params=p)
        string = r.text
        json_str = json.loads(string, encoding=None)
    else:
        if album:
            data = {
                'album':album,
            }
            r = requests.get("https://cscloud.herokuapp.com/api/v1/music/canciones/", params=data)
            string = r.text
            json_str = json.loads(string, encoding=None)    
        else:
            r = requests.get("https://cscloud.herokuapp.com/api/v1/music/canciones/")
            string = r.text
            json_str = json.loads(string, encoding=None)      

    return render(request, "landing/canciones.html", {
        'canciones' : json_str,
        })

def add_artista(request):
    form = AddArtistaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = {
                'nombre': form.cleaned_data['nombre'],
                'nacionalidad' : form.cleaned_data['nacionalidad'],
                'acerca_de': form.cleaned_data['acerca_de'],
                'tipo_artista' : form.cleaned_data['tipo_artista'],
                'genero' : form.cleaned_data['genero'],
                
            }
            r = requests.post("https://cscloud.herokuapp.com/api/v1/artistas/",data=data)
            print(r.status_code)
            r = requests.get("https://cscloud.herokuapp.com/api/v1/artistas")
            string = r.text
            json_str = json.loads(string, encoding=None) 
            return render(request, "landing/artistas.html",{
                'artistas':json_str
            })
        else:
            r = requests.get("https://cscloud.herokuapp.com/api/v1/artistas")
            string = r.text
            json_str = json.loads(string, encoding=None) 
            return render(request, "landing/artistas.html",{
                'artistas':json_str
            })
        

    else:
        return render(request, "landing/add_artista.html", {
            'form':form
        })

def add_album(request):
    form = AddAlbumForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = {
                'nombre': form.cleaned_data['nombre'],
                'anio' : form.cleaned_data['anio'],
                'artista': request.POST['artista'],
                'genero' : form.cleaned_data['genero'],
                
            }
            r = requests.post("https://cscloud.herokuapp.com/api/v1/music/albums/",data=data)
            print(r.status_code)
            r = requests.get("https://cscloud.herokuapp.com/api/v1/music/albums")
            string = r.text
            json_str = json.loads(string, encoding=None) 
            return render(request, "landing/albums.html",{
                'albums':json_str
            })
        else:
            r = requests.get("https://cscloud.herokuapp.com/api/v1/music/albums")
            string = r.text
            json_str = json.loads(string, encoding=None) 
            return render(request, "landing/albums.html",{
                'albums':json_str
            })
        

    else:
        r = requests.get("https://cscloud.herokuapp.com/api/v1/artistas?format=json")
        string = r.text
        json_str = json.loads(string, encoding=None) 
        return render(request, "landing/add_album.html", {
            'form':form,
            'artistas':json_str,
        })
def add_cancion(request):
    generos ={
      "LA":"Latina",
      "PO":"Pop",
      "RO":"Rock",
      "IA":"Indie/Alternativa",
      "DA":"Dance",
      "HH":"Hip Hop",
      "RB":"Rhythm and Blues",
      "CO":"Country",
      "FA":"Folk & Americana",
      "ME": "Metal",
      "SO": "Soul",
      "JA": "Jazz",
      "BL": "Blues",
      "PU": "Punk",
      "FU": "Funk",
      "CL": "Clásica",  
    }
    r = requests.get("https://cscloud.herokuapp.com/api/v1/music/albums")
    string = r.text
    albums = json.loads(string, encoding=None)
    if request.method == 'POST':
        data = {
                'nombre': request.POST['nombre'],
                'anio' : request.POST['anio'],
                'album': request.POST['album'],
                'genero' : request.POST['genero'],
                'rating' : request.POST['rating'],
                
            }
        r = requests.post("https://cscloud.herokuapp.com/api/v1/music/canciones/",data=data)
         
        #print(r.text)
        #print(request.POST['url_cancion'])
        string_cancion = r.text
        cancion_dict = json.loads(string_cancion,encoding=None)
        #print(cancion['id'])
        url = 'https://cscloud.herokuapp.com/api/v1/music/canciones/%s/' % (cancion_dict['id'])
        cancion = {
            'id': cancion_dict['id'],
            'nombre': request.POST['nombre'],
            'anio' : request.POST['anio'],
            'album': request.POST['album'],
            'genero' : request.POST['genero'],
            'rating' : request.POST['rating'],
            'url_cancion': str(request.FILES["url_cancion"])
        }
        r = requests.put(url,data=cancion)
        #print(request.FILES["url_cancion"])
        #file = dict(request.FILES["url_cancion"]).pop()
        files={'file': request.FILES['url_cancion']}
        r = requests.post('https://cscloud.herokuapp.com/api/v1/music/files/',files=files)
        print(r.text)
    return render(request, "landing/add_cancion.html", {
            'albums':albums,
            'generos':generos,
        })

def guarda(request):
    #para guardar archivos con el api
    url = 'https://cscloud.herokuapp.com/api/v1/music/files/'
    files = {'file': open('/home/adrian/logo_unam.png', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)
    
    # para hacer update a la tabla canciones con el api
    url = 'https://cscloud.herokuapp.com/api/v1/music/canciones/1/'
    cancion = {
        "id": 1,
        "nombre": "Cancion 1",
        "anio": 2015,
        "genero": "LA",
        "album": 1,
        "rating": "5.00",
        "url_cancion": "logo_unam.png",
    }
    r = requests.put(url,data=cancion)

    return HttpResponse("guardado")

