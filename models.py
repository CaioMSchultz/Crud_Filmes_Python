from django.db import models

# Create your models here.
class Filmes(models.Model):
    Título = models.CharField(max_length=150)
    Lançamento = models.IntegerField()