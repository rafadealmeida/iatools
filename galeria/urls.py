from django.urls import path
from galeria.views import index
from galeria.views import imagem
from galeria.views import buscar
from galeria.views import contato

urlpatterns = [
    path('', index,name='index'),
    path('imagem/<int:id>/', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('contato/', contato, name='contato'),
]