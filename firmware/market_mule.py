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
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from models import Basket, Item
from time import sleep


class MarketMule:
    _data_gpio = 5
    _sck_gpio = 6
    _base_url = 'http://0.tcp.sa.ngrok.io:12464'
    _weight_detect_offset = 100

    def __init__(self):
        self.hx711 = HX711(self._data_gpio, self._sck_gpio)
        self.camera = PiCamera()
        self.setup()
        self.serial = i2c(port=1, address=0x3C)
        self.device = ssd1306(self.serial)
        self._identified_item = None
        self._last_weight_measure = 0
        self._basket = Basket('default')

    def setup(self):
        self.camera.start_preview()
        self.camera.resolution = (720, 1080)
        self.camera.rotation = 90
        self.camera.brightness = 60
        self.camera.contrast = 20

        while self.camera.analog_gain <= 1:
            time.sleep(0.1)
        self.hx711.tare()

    def clean_and_exit(self):
        print("Cleaning...")
        GPIO.cleanup()
        print("Bye!")
        sys.exit()

    def get_grams(self, is_removing=False) -> float:
        measures = [
            self.hx711.get_grams(1),
            self.hx711.get_grams(1),
            self.hx711.get_grams(1)
        ]

        comparing_function = min if is_removing else max
        measure = comparing_function(measures)

        self.hx711.power_down()
        time.sleep(.001)
        self.hx711.power_up()
        return measure
    
    def display_message(self, message):
        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="white", fill="black")
            draw.text((10, 40), message, fill="white")

    def take_photo(self) -> bytes:
        self.camera.capture('/tmp/picture.jpg')

    def handle_identify_request(self, image_bytes: bytes):
        try:
            ia_url = path.join(self._base_url, 'identify') + '/'
            qrcode_url = path.join(self._base_url, 'qrcode') + '/'
            data = {
                'image': image_bytes
            }
            print('> Making request to:', qrcode_url)
            response = requests.post(qrcode_url, files=data, timeout=30)

            json_response = response.content.decode('utf-8')
            parsed_response = json.loads(json_response)
            
            if response.status_code != 200 or len(parsed_response) == 0:
                print('> Making request to:', ia_url)
                response = requests.post(ia_url, files=data, timeout=30)

            if response.status_code != 200:
                return None

            json_response = response.content.decode('utf-8')
            parsed_response = json.loads(json_response)

            if len(parsed_response) == 0:
                return None

            return parsed_response[0]['name']
        except:
            print('Error on identifying item: API didnt respond')
            return None

    def handle_add_to_basket_request(self, item_name: str, weight: float):
        try:
            url = path.join(self._base_url, 'basket', 'add') + '/'
            print('> Making request to:', url)
            headers = {'Content-Type': 'application/json'}
            data = {
                'name': item_name,
                'weight': weight
            }
            json_data = json.dumps(data)

            response = requests.post(url, data=json_data, headers=headers)

            if response.status_code != 200:
                print("Error: Could not make the add to basket request.")
        except:
            print('Error on adding item: API didnt respond')

    def handle_remove_from_basket_request(self, item_name: str, weight: float):
        try:
            url = path.join(self._base_url, 'basket', 'remove') + '/'
            print('> Making request to:', url)
            headers = {'Content-Type': 'application/json'}
            data = {
                'name': item_name,
                'weight': weight
            }
            json_data = json.dumps(data)

            response = requests.post(url, data=json_data, headers=headers)

            if response.status_code != 200:
                print("Error: Could not make the add to basket request.")
        except:
            print('Error on removing item: API didnt respond')

    def add_to_basket_flow(self, weight_measure: float) -> None:
        item_weight = weight_measure - self._last_weight_measure

        item = Item(self._identified_item, item_weight)
        self._basket.add_item(item)
        self.handle_add_to_basket_request(self._identified_item, item_weight)
        self._last_weight_measure = weight_measure
        self._identified_item = None
        self.display_message("Item added")

    def remove_from_basket_flow(self, weight_measure: float) -> None:
        removed_item = self._basket.remove_item(weight_measure)

        if removed_item is not None:
            self.handle_remove_from_basket_request(removed_item.name, removed_item.weight)
            self._last_weight_measure -= weight_measure
            self.display_message("Item removed")

    def complete_flow(self):
        print('> Taking photo...')
        self.take_photo()
        print('> Identifying item...')

        with open('/tmp/picture.jpg', 'rb') as f:
            identified_item = self.handle_identify_request(f.read())

        if identified_item != '' and identified_item is not None:
            print(f'> Item identified {identified_item}')
            self._identified_item = identified_item
            self.display_message(f"Identified {identified_item}")

        print('> getting weight measure...')
        weight_measure = self.get_grams()
        print(f'> Weight measure found: {weight_measure}')
        # If identified object has been put in the basket
        item_was_added = self._last_weight_measure < weight_measure - self._weight_detect_offset and self._identified_item is not None
        if item_was_added:
            print('> adding item...')
            self.add_to_basket_flow(weight_measure)

        print('> getting weight measure...')
        weight_measure = self.get_grams(is_removing=True)
        print(f'> Weight measure found: {weight_measure}')
        item_was_removed = self._last_weight_measure > weight_measure + self._weight_detect_offset
        if item_was_removed:
            print('> removing item...')
            self.remove_from_basket_flow(self._last_weight_measure - weight_measure)

        time.sleep(1)

    def loop(self):
        running = True
        while running:
            try:
                self.complete_flow()
            except (KeyboardInterrupt, SystemExit):
                self.clean_and_exit()
                running = False

if __name__ == '__main__':
    mm = MarketMule()
    while True:
        print(mm.get_grams())

