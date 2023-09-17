'''
  Install:

  libhx711 # use your package manager to add this lib
  pip3 install --upgrade hx711-rpi-py

  To calibrate:

  There is a Python script in the src directory you can use
  to calibrate your load cell and obtain the reference unit
  and offset values referred to above.
  The simplest way to use it after installing hx711-rpi-py is as follows:

  pi@raspberrypi:~ $ wget https://github.com/endail/hx711-rpi-py/blob/master/src/calibrate.py
  pi@raspberrypi:~ $ python3 calibrate.py [data pin] [clock pin]
'''

from HX711 import *

# DT -> 3
# SCK -> 5
dt_pin = 3
sck_pin = 5
reference_unit = -370
calibrated_offset = -367471

def measure_weight():
  with SimpleHX711(dt_pin, sck_pin, reference_unit, calibrated_offset) as hx:
    hx.setUnit(Mass.Unit.KG)
    hx.zero()
    measure_value = hx.weight(35)
  return measure_value


if __name__ == '__main__':
  with SimpleHX711(dt_pin, sck_pin, reference_unit, calibrated_offset) as hx:

    # set the scale to output weights in ounces
    hx.setUnit(Mass.Unit.KG)

    # zero the scale
    hx.zero()

    # constantly output weights using the median of 35 samples
    while True:
      print(hx.weight(35))