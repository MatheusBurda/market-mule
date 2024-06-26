from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Basket, Item
from . import identify_service
import json
from .products import products

@csrf_exempt
def identify_object(request):
  image_blob = request.FILES.get('image').file.read()
  print(request.FILES)
  identified_objects = identify_service.identify_object(image_blob)
  
  objects_with_price = []
  if identified_objects is not None:
    # current_basket = Basket('default')
    for object in identified_objects:
      if '_' in object:
        object = object.split('_')[1]
      if object in products.keys():
        print(object)
        # current_basket.add_item(item)
        objects_with_price.append({
          'name': object,
          'price': products[object]['price']
        })

  response_json = json.dumps(objects_with_price)
  return HttpResponse(response_json, content_type="application/json")

@csrf_exempt
def read_qrcode(request):
  uploaded_file = request.FILES.get('image')
  image_blob = uploaded_file.read()
  identified_objects = identify_service.identify_by_qrcode(image_blob)

  objects_with_price = []
  if identified_objects is not None:
    # current_basket = Basket('default')
    for object in identified_objects:
      if object in products.keys():
        # current_basket.add_item(item)
        objects_with_price.append({
          'name': object,
          'price': products[object]['price']
        })

  response_json = json.dumps(objects_with_price)
  return HttpResponse(response_json, content_type="application/json")

def basket(request):
  current_basket = Basket('default')
  return HttpResponse(current_basket.to_json(), content_type="application/json")

@csrf_exempt
def add_item(request):
  current_basket = Basket('default')
  item_dict = json.loads(request.body)
  
  if item_dict['name'] not in products.keys():
    return HttpResponse(content = {'Error': 'Product not found!'}, content_type="application/json", status=404)
  
  item = Item(item_dict['name'], item_dict['weight'])
  current_basket.add_item(item)

  return HttpResponse(current_basket.to_json(), content_type="application/json")

@csrf_exempt
def remove_item(request):
  current_basket = Basket('default')
  item_dict = json.loads(request.body)

  if item_dict['name'] not in products.keys():
    return HttpResponse(content = {'Error': 'Product not found!'}, content_type="application/json", status=404)

  current_basket.remove_item(item_dict['name'], item_dict['weight'])

  return HttpResponse(current_basket.to_json(), content_type="application/json")
