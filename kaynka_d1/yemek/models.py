from django.db import models

class Makale(models.Model):
    baslik=models.CharField(max_length=50)
    icerik=models.TextField()
