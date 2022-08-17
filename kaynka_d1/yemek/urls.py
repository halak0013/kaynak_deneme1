from django.urls import path,include
from .views import yemek_gorunum
urlpatterns = [
    path("yemek/", yemek_gorunum),
]
