from django.urls import path
from . import views
from .api import api

urlpatterns = [
    path('api/', api.urls),
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('add', views.add, name='añadir'),
    path('mens_clothing', views.mens_clothing, name='mens_clothing'),
    path('womens_clothing', views.womens_clothing, name='womens_clothing'),
    path('electronics', views.electronics, name='electronics'),
    path('jewelery', views.jewelery, name='jewelery'),
    path('consultas', views.consultas, name='consultas'),
    path('consulta1', views.consulta1, name='consulta1'),
    path('consulta2', views.consulta2, name='consulta2'),
    path('consulta3', views.consulta3, name='consulta3'),
    path('consulta4', views.consulta4, name='consulta4'),
    path('consulta5', views.consulta5, name='consulta5'),
    path('consulta6', views.consulta6, name='consulta6')
]