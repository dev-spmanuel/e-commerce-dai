from ninja_extra import NinjaExtraAPI
from bson import ObjectId
from pydantic import BaseModel as Schema
from pymongo import ReturnDocument
from .models import connect, get_product_by_id
from ninja.security import HttpBearer
import json
import logging
logger = logging.getLogger(__name__)

class GlobalAuth(HttpBearer):
  def authenticate(self, request, token):
    if token == "supersecret":
      return token

api = NinjaExtraAPI()
# api = NinjaExtraAPI(auth=GlobalAuth())

tienda = connect()
productos_collection = tienda.productos

class Rate(Schema):
	rate: float
	count: int
	
class ProductSchema(Schema):  # sirve para validar y para documentación
	title: str
	price: float
	description: str
	category: str
	image: str = None
	rating: Rate = None
	
class ProductSchemaIn(Schema):
  title: str
  price: float
  category: str
  description: str
	
class ErrorSchema(Schema):
  message: str

@api.get('/producto', tags=['TIENDA DAI'])
def get_products(request, desde: int = 0, hasta: int = 100):
  products = productos_collection.find().skip(desde).limit(hasta-desde)
  products_list = [{**product, '_id': str(product['_id'])} for product in products]
  return list(products_list)

@api.get('/producto/{id}', tags=['TIENDA DAI'])
def get_product(request, id: str):
  product = productos_collection.find_one({'_id': ObjectId(id)})
  return {**product, '_id': str(product['_id'])}

@api.post('/producto', tags=['TIENDA DAI'])
def create_product(request, payload: ProductSchemaIn):
  payload_dict = payload.dict()
  id = str(productos_collection.insert_one(payload_dict).inserted_id)
  return "id: " + id

@api.put('/producto/{id}', tags=['TIENDA DAI'], response={202: ProductSchema, 400:ErrorSchema, 404: ErrorSchema})
def update_product(request, id: str, payload: ProductSchemaIn):
  try:
    updated_product = productos_collection.find_one_and_update(
      {'_id': ObjectId(id)},
      {'$set': payload.dict()},
      return_document=ReturnDocument.AFTER
    )
    if updated_product:
      return 202, updated_product 
    else:
      return 400, {"message": "no actualizado"}
  except:
    return 404, {'message': 'no encontrado'}

@api.delete('/producto/{id}', tags=['TIENDA DAI'])
def delete_product(request, id: str):
  deleted = str(productos_collection.delete_one({'_id': ObjectId(id)}).deleted_count)
  return ("borrados: " + deleted)

@api.post('/producto/{id}/rate', tags=['TIENDA DAI'], response={202: ProductSchema})
def rate_product(request, id: str, rate: Rate):
  updated_product = productos_collection.find_one_and_update(
    {'_id': ObjectId(id)},
    {'$set': {'rating': rate.dict()}},
    return_document=ReturnDocument.AFTER
  )
  return 202, updated_product