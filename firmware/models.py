from django.db import models
import json

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
      grouped_item = {
        'name': item['name'],
        'weights': []
      }
      for _ in range(item['quantity']):
        grouped_item['weights'].append(item['weight'])
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
