from django.urls import path

from .views import home
from .views import categorias


urlpatterns = [   
    path('', home, name='home'),
    path('categoria/<categoria_id>', categorias, name='categoria')
]
