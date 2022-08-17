from django.contrib import admin
from django.urls import path,include

from eicerik.views import kitap_olustur
urlpatterns = [
    path('admin/', admin.site.urls),
    path("yemek/", include("yemek.urls")),
]
