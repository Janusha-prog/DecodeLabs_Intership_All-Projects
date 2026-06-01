# Project-4
# DecodeLabs-Proj4-Image-Text-Recognition
A Python-based OCR project that reads text from images using OpenCV and Tesseract OCR, with preprocessing techniques to improve text detection accuracy.

# Project Overview
This project is an Optical Character Recognition (OCR) system developed using Python, OpenCV, and Tesseract OCR. The goal of this project is to extract text from images and convert it into machine-readable text.
The system reads an image, applies image preprocessing techniques, and uses OCR technology to detect and extract text from the image.
For demonstration, a stock market summary image was used as input, and the system successfully extracted the textual information present in the image.

# Technologies Used
* Python 3
* OpenCV (cv2)
* Pytesseract
* Tesseract OCR Engine

# Libraries Installed
# OpenCV 
Used for:
* Reading images
* Image preprocessing
* Grayscale conversion
* Thresholding

# Pytesseract
Used for:
* Text extraction from images

# Tesseract OCR Software
Installed Tesseract OCR Engine separately and connected it with Python.
Default installation path:
C:\Program Files\Tesseract-OCR\tesseract.exe

# Project Workflow
# Step 1: Load Image
The input image is loaded using OpenCV.

# Step 2: Convert Image to Grayscale
The image is converted into grayscale to improve OCR accuracy.

# Step 3: Apply Image Preprocessing
Adaptive Thresholding is applied to separate text from the background and reduce noise.

# Step 4: Extract Text
Pytesseract OCR is used to recognize and extract text from the processed image.

# Step 5: Save OCR Output
The extracted text is:
* Displayed in the terminal
* Saved into a text file

# Step 6: Save Processed Image
The thresholded image is saved for visual verification and analysis.

# Features
* Image to Text Conversion
* OCR-based Text Recognition
* Grayscale Preprocessing
* Adaptive Thresholding
* Text Output Generation
* Processed Image Generation
* Beginner-Friendly Implementation

# Files Generated
# Input Image
The image provided to the OCR system.

# Processed Image
Generated after preprocessing and thresholding.

# Output Text File
Contains the text extracted from the image using OCR.

# Concepts Learned
Through this project, I learned:
* Optical Character Recognition (OCR)
* Image Preprocessing
* Grayscale Conversion
* Adaptive Thresholding
* Text Extraction from Images
* OpenCV Basics
* Tesseract OCR Integration
* Python File Handling

# Sample Use Cases
* Document Digitization
* Invoice Processing
* Text Extraction from Images
* Data Entry Automation
* Image Analysis Systems

# Conclusion
This project helped me understand how machines can recognize and extract text from images using OCR technology. It provided hands-on experience with image preprocessing, OpenCV, Tesseract OCR, and text extraction techniques used in many real-world AI applications.

