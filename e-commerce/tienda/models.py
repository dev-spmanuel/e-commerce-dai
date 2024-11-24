from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
# from django.db import models
from datetime import datetime
from pymongo import MongoClient
from collections import defaultdict

# ---------------- Modelos de datos ----------------
class Rate(BaseModel):
	rate: float = Field(ge=0., lt=5.)
	count: int = Field(ge=1)
class Product(BaseModel):
  title: str
  price: float
  description: str
  category: str
  image: Optional[str]
  rating: Optional[Rate]

  @validator('title')
  @classmethod
  def title_must_be_upper(cls, v: str) -> str:
    if not v[0].isupper():
      raise ValueError('title must be upper case')
    return v

class Order(BaseModel):
	user: EmailStr
	date: datetime
	products: list	



# ----------- connect to DB -----------
def connect():
  print('Connecting to DB...')
  client = MongoClient('mongo', 27017)
  tienda_db = client.tienda
  return tienda_db

# ----------------- Insertar -----------------
# Productos
def insertProduct(productos_collection, product):
  # imagePath = product['image']
  # product['image'] = imagePath[24:]
  # del product['id']
  # del product['rating']
  p = Product(**product)
  productos_collection.insert_one(p.dict())

def insertProducts(productos_collection, productos):
  for p in productos:
    # imagePath = p['image']
    # p['image'] = imagePath[24:]
    # del p['id']
    # del p['rating']
    product = Product(**p)
    productos_collection.insert_one(product.dict())

# Compras
def insertOrder(compras_collection, order):
  c = Order(**order)
  compras_collection.insert_one(c.dict())

# ----------------- Eliminar -----------------
# Productos
def deleteProduct(productos_collection, id):
  productos_collection.delete_one({'_id': id})

def deleteProducts(productos_collection):
  productos_collection.delete_many({})

# ----------------- Obtener por categorias -----------------
def get_mens_clothing(productos_collection):
  productos = []
  for p in productos_collection.find({'category': "men's clothing"}):
    if p['rating'] is not None:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id']), p['rating']['rate'], p['rating']['count']])
    else:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id'])])
  
  return productos

def get_womens_clothing(productos_collection):
  productos = []
  for p in productos_collection.find({'category': "women's clothing"}):
    if p['rating'] is not None:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id']), p['rating']['rate'], p['rating']['count']])
    else:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id'])])
  
  return productos

def get_electronics(productos_collection):
  productos = []
  for p in productos_collection.find({'category': "electronics"}):
    if p['rating'] is not None:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id']), p['rating']['rate'], p['rating']['count']])
    else:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id'])])
  
  return productos

def get_jewelery(productos_collection):
  productos = []
  for p in productos_collection.find({'category': "jewelery"}):
    if p['rating'] is not None:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id']), p['rating']['rate'], p['rating']['count']])
    else:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id'])])
    
  return productos

# ----------------- Obtener por nombre -----------------
def get_products_by_name(productos_collection, name):
  productos = []
  for p in productos_collection.find({
    '$or':[
      {'title': {'$regex': name, '$options': 'i'}},
      {'description': {'$regex': name, '$options': 'i'}},
      {'category': {'$regex': name, '$options': 'i'}}
    ]
  }):
    if p['rating'] is not None:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id']), p['rating']['rate'], p['rating']['count']])
    else:
      productos.append([p['title'], p['description'], p['price'], p['image'], p['category'], str(p['_id'])])
  
  return productos

# ----------------- Obtener por id -----------------

def get_product_by_id(productos_collection, id):
  product = productos_collection.find_one({'_id': id})
  return product

# ----------------- Obtener media de rating -----------------
# calcular la media de rating de un producto
def get_rating_average(productos_collection, id):
  product = productos_collection.find_one({'_id': id})
  if product['rating'] is not None:
    return product['rating']['rate']
  else:
    return 0.0


# ----------------- Consultas -----------------
def c1 (productos_collection):
  productos = []
  for p in productos_collection.find({'category': 'electronics', 'price': {'$gt': 100.0, '$lt': 200.0}}).sort('price'):
    productos.append([p['title'], p['description'], p['category'], p['price'], p['rating']['rate'], p['rating']['count']])
  return productos

def c2 (productos_collection):
  productos = []
  for p in productos_collection.find({'description': {'$regex': 'pocket', '$options': 'i'}}):
    productos.append([p['title'], p['description'], p['category'], p['price'], p['rating']['rate'], p['rating']['count']])
  return productos

def c3 (productos_collection):
  productos = []
  for p in productos_collection.find({'rating.rate': {'$gt': 4.0}}):
    productos.append([p['title'], p['description'], p['category'], p['price'], p['rating']['rate'], p['rating']['count']])
  return productos

def c4 (productos_collection):
  productos = []
  for p in productos_collection.find({'category': "men's clothing"}).sort('rating.rate', -1):
    productos.append([p['title'], p['description'], p['category'], p['price'], p['rating']['rate'], p['rating']['count']])
  return productos

def c5 (productos_collection, compras_collection):
  facturacion = 0.0
  for c in compras_collection.find({}):
    for p in c['productos']:
      prod = productos_collection.find_one({'_id': p})
      if prod != None:
        facturacion += prod['price']

  return facturacion

def c6 (productos_collection, compras_collection):
  facturacion_categorias = defaultdict(float)

  for c in compras_collection.find({}):
    for p in c['productos']:
      prod = productos_collection.find_one({'_id': p})
      if prod != None:
        facturacion_categorias[prod.get('category')] += prod.get('price')

  return facturacion_categorias