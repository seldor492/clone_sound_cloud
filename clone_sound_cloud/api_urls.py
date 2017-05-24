from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_swagger.views  import get_swagger_view
schema_view = get_swagger_view(title="csoundcloud API")


urlpatterns = [
    url(r'^artistas/', include("modules.Artistas.urls")),
    url(r'^music/', include("modules.music.urls")),
    url(r'^users/', include("modules.Users.urls")),
    url(r'^docs/', schema_view,name='docs'),
]