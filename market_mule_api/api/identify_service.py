import cv2
import numpy
import qrcode
from yolo import yolo

def identify_object(image_path) -> list:
  timeout = 40 #seconds
  yolo(timeout,image_path)
  objects = yolo.run()
  return objects

def identify_by_qrcode(image_blob):
  try:
    # Read the image from the image_blob (e.g., a binary image file)
    image = cv2.imdecode(numpy.frombuffer(image_blob , numpy.uint8), cv2.IMREAD_ANYCOLOR)

    # Detect QR codes in the image
    detector = cv2.QRCodeDetector()
    _, decoded_info, _, _ = detector.detectAndDecodeMulti(image)
    
    if len(decoded_info) > 0:
      qrcode_info = list(filter(lambda info : len(info) > 0, decoded_info))[0]
      # Return the decoded QR code information
      return qrcode_info

    # If no QR code is detected, return None
    return None
  
  except Exception as e:
    # Handle any exceptions that may occur during processing
    print(f"An error occurred: {e}")
    return None