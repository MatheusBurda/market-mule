import json
import math
from django.db import models

from .products import products

class Item:
  def __init__(self, name: str, weight: float):
    self.name = name
    self.weight = weight
    self.quantity = 1
  

  def get_key(self):
    return (self.name.strip(), int(self.weight))
  

  def to_dict(self):
    return {
      'name': self.name,
      'weight': self.weight,
      'quantity': self.quantity
    }

class Basket:
  _instance = None

  def __new__(cls, name):
    if cls._instance is None:
      cls._instance = super(Basket, cls).__new__(cls)
      cls._instance.name = name
      cls._instance.items = {}
    return cls._instance

  def add_item(self, item: Item):
    key = item.get_key()
    currentItem = self.items.get(key)
    
    if currentItem is None:
      self.items[key] = item
      return

    currentItem.quantity += 1

  def get_closest_weight_item(self, name: str, target_weight: float):
    closest_item = None
    min_weight_difference = float('inf')

    for key, item in self.items.items():
      if item.name.strip() == name.strip():
        weight_difference = abs(item.weight - target_weight)
        if weight_difference < min_weight_difference:
          closest_item = item
          min_weight_difference = weight_difference

    return closest_item
  
  
  def remove_item(self, name: str, weight: float):
    closest_item = self.get_closest_weight_item(name, weight)
    if closest_item:
      key_to_remove = closest_item.get_key()
      item = self.items[key_to_remove]

      if item.quantity == 1:
        del self.items[key_to_remove]
      else:
        item.quantity -= 1
      print(f"Removed item: {closest_item.name}, Weight: {closest_item.weight}")
    else:
      print("No matching items found.")
  
  def to_json(self):
    items_list = list(self.items.values())
    items_dict_list = list(map(lambda item: item.to_dict(), items_list))
    
    flat_item_list = []
    for item in items_dict_list:

      index = next((i for i, it in enumerate(flat_item_list) if it["name"] == item['name']), None)
      
      grouped_item = {
        'name': item['name'],
        'weights': [],
        'prices': [],
        'quantity': 0,
        'total_price': 0,
        'total_weight': 0,
        'image': 'src/assets/undefined.jpg'
      } if index is None else flat_item_list.pop(index)

      product =  products[item['name']]

      grouped_item['weights'] += [item['weight'] for _ in range(item['quantity'])]
      grouped_item['weights'] = sorted(grouped_item['weights'])
      grouped_item['quantity'] = len(grouped_item['weights'])
      
      grouped_item['prices'] = []
      for weight in grouped_item['weights']:
        price = product["price"] if product["default-weight"] == True else weight * product["price"] / 1e3
        price = round(price, 2)
        grouped_item['prices'].append(price)

      grouped_item['quantity'] = len(grouped_item['weights'])
      grouped_item['total_price'] = sum(grouped_item['prices'])
      grouped_item['total_weight'] = sum(grouped_item['weights'])
      grouped_item['image'] = product['image']

      flat_item_list.append(grouped_item)

    response = {
      'name': self.name,
      'items': flat_item_list
    }

    return json.dumps(response)


if __name__ == '__main__':
  basket = Basket('jose')
  item = Item('banana', 123.32)

  basket.add_item(item)
  basket.add_item(item)
  basket.add_item(item)
  basket.add_item(item)
  basket.remove_item('banana', 145)

  banana_pesada = Item('banana', 533)
  basket.add_item(banana_pesada)
  basket.add_item(banana_pesada)
  basket.add_item(banana_pesada)

  print (basket.items[('banana', 123)].quantity)
