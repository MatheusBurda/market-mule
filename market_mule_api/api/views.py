from django.shortcuts import render
from django.http import HttpResponse
from .models import Basket, Item
import json
        
def basket(request):
    current_basket = Basket('default')
    return HttpResponse(current_basket.to_json(), content_type="application/json")

def add_item(request):
  return HttpResponse('', content_type="application/json")

def remove_item(request):
  return HttpResponse('', content_type="application/json")

def identify_object(request):
  return HttpResponse('', content_type="application/json")
