from HX711 import *

# DT -> 3
# SCK -> 5
calibrated_offset = -367471
with SimpleHX711(3, 5, -370, calibrated_offset) as hx:

  # set the scale to output weights in ounces
  hx.setUnit(Mass.Unit.OZ)

  # zero the scale
  hx.zero()

  # constantly output weights using the median of 35 samples
  while True:
    print(hx.weight(35)) #eg. 1.08 oz