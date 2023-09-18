from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Basket
from .identify_service import *
import json


@csrf_exempt
def identity_object(request):
  image_blob = request.FILES.get('image')
  identified_object = identify_object(image_blob)

  response_json = json.dumps({
    "object": identified_object
  })
  return HttpResponse(response_json, content_type="application/json")

@csrf_exempt
def read_qrcode(request):
  uploaded_file = request.FILES.get('image')
  image_blob = uploaded_file.read()
  identified_object = identify_by_qrcode(image_blob)

  response_json = json.dumps({
    "object": identified_object
  })
  return HttpResponse(response_json, content_type="application/json")

def basket(request):
  current_basket = Basket('default')
  return HttpResponse(current_basket.to_json(), content_type="application/json")

def add_item(request):
  return HttpResponse('', content_type="application/json")

def remove_item(request):
  return HttpResponse('', content_type="application/json")

def identify_object(request):
  return HttpResponse('', content_type="application/json")
