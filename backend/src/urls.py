from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as autodoc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('url_shortener_app.urls')),
]

urlpatterns += autodoc
