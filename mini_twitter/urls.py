from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from authenticate.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authenticate.urls.authUrls')),
    path('profile/', include('authenticate.urls.profileUrls')),
    path('search/', include('authenticate.urls.searchUrls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
