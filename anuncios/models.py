from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=40)