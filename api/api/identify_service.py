import cv2
import numpy
import qrcode
from ultralytics import YOLO

model = YOLO("yolov8n.pt","predict")

def identify_object(image_blob) -> list:
  #Thread for identify obj are done on yolo.py
  #see the example for the utilization
  image = cv2.imdecode(numpy.frombuffer(image_blob , numpy.uint8), cv2.IMREAD_ANYCOLOR)
  results = model.predict(source=image.copy(),stream=True,save=True)
  
  items = []
  for result in results:
    if result.boxes:
        box = result.boxes[0]
        class_id = int(box.cls)
        object_name = model.names[class_id]
        items.append(object_name)

  return items 
  

def identify_by_qrcode(image_blob):
  try:
    # Read the image from the image_blob (e.g., a binary image file)
    image = cv2.imdecode(numpy.frombuffer(image_blob , numpy.uint8), cv2.IMREAD_ANYCOLOR)

    # Detect QR codes in the image
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(image)
    print('> QR CODE RESULT:', value)
    
    if len(value) > 0:
      # Return the decoded QR code information
      return [value]

    # If no QR code is detected, return None
    return []
  
  except Exception as e:
    # Handle any exceptions that may occur during processing
    print(f"An error occurred: {e}")
    return []
  
if __name__ == "__main__":
  with open("/home/hellhat/market-mule/market_mule_api/api/assets/maca.jpeg","rb") as file:
    identify_object(file.read())