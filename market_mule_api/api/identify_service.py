import cv2
import qrcode

def identify_object(image_blob) -> str:
  # TODO: Implement here the logics for the image blob
  # it shoulds return a string of the main object identified
  pass

def identify_by_qrcode(image_blob):
  try:
    # Read the image from the image_blob (e.g., a binary image file)
    image = cv2.imdecode(image_blob, cv2.IMREAD_COLOR)

    # Detect QR codes in the image
    detector = cv2.QRCodeDetector()
    decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(image)

    if decoded_info:
      # Return the decoded QR code information
      return decoded_info

    # If no QR code is detected, return None
    return None
  
  except Exception as e:
    # Handle any exceptions that may occur during processing
    print(f"An error occurred: {e}")
    return None