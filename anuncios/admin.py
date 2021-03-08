from django.contrib import admin

from anuncios import models
# Register your models here.

admin.site.register(models.Categoria)
admin.site.register(models.Anuncio)