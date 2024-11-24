from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import connect, c1, c2, c3, c4, c5, c6
from .models import get_mens_clothing, get_womens_clothing, get_electronics, get_jewelery
from .models import get_products_by_name
from .models import insertProduct
from django.contrib import messages
from .forms import ProductoForm, LoginForm
import os
from django.conf import settings
import logging
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

tienda_db = connect()
productos_collection = tienda_db.productos
compras_collection = tienda_db.compras

# ------------- Rutas -------------
class Home(TemplateView):
  def dispatch(self, request, *args, **kwargs):
    return HttpResponseRedirect('/tienda')

def index(request):
  context = {}
  return render(request, 'tienda/index.html', context)

def buscar(request):
  productos = get_products_by_name(productos_collection, request.GET['busqueda'])

  context = {
    'busqueda': request.GET['busqueda'],
    'productos': productos
  }
  return render(request, 'tienda/busqueda.html', context)

def add(request):
  form = ProductoForm()

  if(request.method == 'POST'):
    form = ProductoForm(request.POST, request.FILES)
    if(form.is_valid()):
      logger.debug(form.cleaned_data)
      logger.debug(request.FILES)
      messages.add_message(request, messages.INFO, 'Producto añadido correctamente')

      image = form.cleaned_data["image"]
      image_name = image.name
      image_path = os.path.join(settings.BASE_DIR, 'static', 'img', image_name)
      with open(image_path, "wb") as destination:
        for chunk in image.chunks():
          destination.write(chunk)

      form.cleaned_data["image"] = 'img/' + image_name

      ## guardar en DB
      insertProduct(productos_collection, form.cleaned_data)
      return redirect('index')

  context = {
    'form': form
  }
  return render(request, 'tienda/añadir.html', context)

def mens_clothing(request):
  productos = get_mens_clothing(productos_collection)
  return render(request, 'tienda/productos.html', {'productos': productos})

def womens_clothing(request):
  productos = get_womens_clothing(productos_collection)
  return render(request, 'tienda/productos.html', {'productos': productos})

def electronics(request):
  productos = get_electronics(productos_collection)
  return render(request, 'tienda/productos.html', {'productos': productos})

def jewelery(request):
  productos = get_jewelery(productos_collection)
  return render(request, 'tienda/productos.html', {'productos': productos})

def consultas(request):
  response = HttpResponse('<html><body><h1>Página de consultas</h1>')
  response.write('<p><a href="../consulta1/">Consulta 1</a></p>')
  response.write('<p><a href="../consulta2/">Consulta 2</a></p>')
  response.write('<p><a href="../consulta3/">Consulta 3</a></p>')
  response.write('<p><a href="../consulta4/">Consulta 4</a></p>')
  response.write('<p><a href="../consulta5/">Consulta 5</a></p>')
  response.write('<p><a href="../consulta6/">Consulta 6</a></p>')

  response.write('</body></html>')
  return response

def consulta1(request):
  productos = c1(productos_collection)

  response = HttpResponse()
  headerConsult(response)
  response.write('<h1>Consulta 1</h1>')
  response.write('<h2>Electrónica entre 100€ y 200€, ordenado por precio</h2>')
  showProducts(productos, response)
  
  response.write('</body></html>')
  return response

def consulta2(request):
  productos = c2(productos_collection)

  response = HttpResponse('<html><body><a href="../">Volver</a>')
  response.write('<h1>Consulta 2</h1>')
  response.write('<h2>Productos que contengan la palabra `pocket` en la descripción</h2>')
  showProducts(productos, response)
  
  response.write('</body></html>')
  return response

def consulta3(request):
  productos = c3(productos_collection)

  response = HttpResponse('<html><body><a href="../">Volver</a>')
  response.write('<h1>Consulta 3</h1>')
  response.write('<h2>Productos con puntuación mayor de 4</h2>')
  showProducts(productos, response)
  
  response.write('</body></html>')
  return response

def consulta4(request):
  productos = c4(productos_collection)

  response = HttpResponse('<html><body><a href="../">Volver</a>')
  response.write('<h1>Consulta 4</h1>')
  response.write('<h2>Ropa de hombre, ordenada por puntuación</h2>')
  showProducts(productos, response)
  
  response.write('</body></html>')
  return response

def consulta5(request):
  facturacion = c5(productos_collection, compras_collection)

  response = HttpResponse('<html><body><a href="../">Volver</a>')
  response.write('<h1>Consulta 5</h1>')
  response.write('<h2>Facturación total</h2>')
  response.write(f'<p> ${facturacion} </p>')

  response.write('</body></html>')
  return response  

def consulta6(request):
  categories = c6(productos_collection, compras_collection)

  response = HttpResponse('<html><body><a href="../">Volver</a>')
  response.write('<h1>Consulta 6</h1>')
  response.write('<h2>Facturación por categoría de producto</h2>')
  showFactCategories(categories, response)

  response.write('</body></html>')
  return response

# -------- Métodos auxiliares para la vista de las consultas --------
def headerConsult(response):
  response.write('<html><body><a href="../">Volver</a>')

def showProducts(products, response):
  for p in products:
    response.write('<p> ------------------------- </p>')
    response.write(f'<p>Title: {p[0]} </p>')
    response.write(f'<p>Description: {p[1]}</p>')
    response.write(f'<p>Category: {p[2]}</p>')
    response.write(f'<p>Price : {p[3]} $</p>')
    response.write(f'<p>Rate: {p[4]} </p>')
    response.write(f'<p>Count_Rate: {p[5]} </p>')

def showFactCategories(categories, response):
  for c, v in categories.items():
    response.write(f'<p>{c}: ${v}</p>')
