import json
from hx711 import HX711
from picamera import PiCamera
from os import path
import RPi.GPIO as GPIO
import time
import sys
import io
import requests
from models import Basket, Item


class MarketMule:
    _data_gpio = 5
    _sck_gpio = 6
    _base_url = 'http://localhost:8000'
    _weight_detect_offset = 100

    def __init__(self):
        self.hx711 = HX711(self._data_gpio, self._sck_gpio)
        self.camera = PiCamera()
        self.setup()
        self._identified_item = None
        self._last_weight_measure = 0
        self._basket = Basket('default')

    def setup(self):
        self.camera.start_preview()

    def clean_and_exit(self):
        print("Cleaning...")
        GPIO.cleanup()
        print("Bye!")
        sys.exit()

    def get_grams(self) -> float:
        measure = self.hx711.get_grams()
        self.hx711.power_down()
        time.sleep(.001)
        self.hx711.power_up()
        return measure

    def take_photo(self) -> bytes:
        image_bytes = io.BytesIO()
        self.camera.capture(image_bytes, 'jpg')
        return image_bytes.read()

    def handle_identify_request(self, image_bytes: bytes) -> str | None:
        url = path.join(self._base_url, 'identify')
        data = {
            'file': image_bytes
        }
        response = requests.post(url, data=data)

        if response.status_code != 200:
            return None

        json_response = response.content.decode('utf-8')
        # { object: "object_name" }
        parsed_response = json.loads(json_response)
        return parsed_response['object']

    def handle_add_to_basket_request(self, item_name: str, weight: float):
        url = path.join(self._base_url, 'add') + '/'
        headers = {'Content-Type': 'application/json'}
        data = {
            'name': item_name,
            'weight': weight
        }
        json_data = json.dumps(data)

        response = requests.post(url, data=json_data, headers=headers)

        if response.status_code != 200:
            print("Error: Could not make the add to basket request.")

    def handle_remove_from_basket_request(self, item_name: str, weight: float):
        url = path.join(self._base_url, 'remove') + '/'

        headers = {'Content-Type': 'application/json'}
        data = {
            'name': item_name,
            'weight': weight
        }
        json_data = json.dumps(data)

        response = requests.post(url, data=json_data, headers=headers)

        if response.status_code != 200:
            print("Error: Could not make the add to basket request.")

    def add_to_basket_flow(self, weight_measure: float) -> None:
        item_weight = self._last_weight_measure - weight_measure

        item = Item(self._identified_item, item_weight)
        self._basket.add_item(item)
        self.handle_add_to_basket_request(self._identified_item, item_weight)
        self._last_weight_measure = weight_measure
        self._identified_item = None

    def remove_from_basket_flow(self, weight_measure: float) -> None:
        removed_item = self._basket.remove_item(weight_measure)

        if removed_item is not None:
            self.handle_remove_from_basket_request(removed_item.name, removed_item.weight)

    def complete_flow(self):
        weight_measure = self.get_grams()
        print(f"Weight Measure: {weight_measure}g")
        image_bytes = self.take_photo()
        identified_item = self.handle_identify_request(image_bytes)

        if self._identified_item != '' and self._identified_item is not None:
            self._identified_item = identified_item

        # If identified object has been put in the basket
        item_was_added = self._last_weight_measure >= weight_measure + self._weight_detect_offset and self._identified_item is not None
        if item_was_added:
            self.add_to_basket_flow(weight_measure)

        item_was_removed = self._last_weight_measure <= weight_measure - self._weight_detect_offset
        if item_was_removed:
            self.remove_from_basket_flow(weight_measure)

        time.sleep(1)

    def loop(self):
        running = True
        while running:
            try:
                self.complete_flow()
            except (KeyboardInterrupt, SystemExit):
                self.clean_and_exit()
                running = False
