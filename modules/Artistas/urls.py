from django.conf.urls import url #agrego include
from django.contrib import admin
from .views import ListArtista,DetailArtista
urlpatterns = [
    url(r'^$', ListArtista.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DetailArtista.as_view())
]