import os
from google.cloud import vision

# set your credentials JSON file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

# Initialize Vision API client
vision_client = vision.ImageAnnotatorClient()

# Open your image file
with open('image.jpg', 'rb') as img:
    content = img.read()

# Perform OCR
image = vision.Image(content=content)
response = vision_client.text_detection(image=image)

# Get extracted text
extracted_text = response.full_text_annotation.text

# Print the result
print("Extracted Text:")
print(extracted_text)
