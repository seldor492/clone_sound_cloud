from django.conf.urls import url #agrego include
from django.contrib import admin
from .views import ListUser,DetailUser
urlpatterns = [
    url(r'^$', ListUser.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DetailUser.as_view())
]