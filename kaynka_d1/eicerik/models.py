from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    yazar = models.ForeignKey(Author, on_delete=models.CASCADE)
    baslık = models.CharField(max_length=100)
    sayfa_sayısı = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
