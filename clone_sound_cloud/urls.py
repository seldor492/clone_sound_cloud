from django.conf.urls import url,include #agrego include
from django.contrib import admin
import csoundcloud.api_urls as api_urls#hago este import
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_urls)),
    url(r'^', include('modules.landing.urls', namespace="landing"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
