from django.conf.urls import url
from .views import index, dashboard, artistas, albums, canciones, add_artista, add_album, guarda, add_cancion

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^artistas/$', artistas, name="artistas"),
    url(r'^albums/$', albums, name="albums"),
    url(r'^canciones/$', canciones, name="canciones"),
    url(r'^artistas/(?P<id>[0-9]+)$', artistas, name="artistas_find"),
    url(r'^canciones/(?P<album>[0-9]+)$', canciones, name="canciones_find"),
    url(r'^albums/(?P<artista>[0-9]+)$',albums, name="albums_find"),
    url(r'^artistas/add_artista/$', add_artista, name="add_artista"),
    url(r'^albums/add_album/$', add_album, name="add_album"),
    url(r'^canciones/add_cancion/$', add_cancion, name="add_cancion"),
    url(r'^guarda/$', guarda, name="guarda"),

]
