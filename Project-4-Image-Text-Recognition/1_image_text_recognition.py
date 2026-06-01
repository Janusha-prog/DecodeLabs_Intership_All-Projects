# Project 4: OCR Text Recognition System

import cv2
import pytesseract

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print("===== STOCK MARKET OCR ANALYSIS =====\n")

# Load image
image = cv2.imread(
    r"C:\Users\qulabs.ai\OneDrive - Qulabs\Desktop\project-4\input_sample_image.png"
)

# Check if image exists
if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# Apply adaptive thresholding
threshold = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# Extract text using OCR
detected_text = pytesseract.image_to_string(threshold)

# Save detected text to a text file
with open("Output_DetectedText.txt", "w", encoding="utf-8") as file:
    file.write(detected_text)

print("Detected text saved successfully!")

# Display extracted text
print("===== DETECTED TEXT =====\n")

if detected_text.strip():
    print(detected_text)
else:
    print("No text detected.")

print("\n=========================")

# Save processed image
cv2.imwrite(
    "processed_image.png",
    threshold
)

print("\nProcessed image saved successfully!")
print("File Name: processed_image.png")
