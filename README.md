# EXIF Metadata Viewer 

This Python script reads and displays *EXIF metadata* from JPG image files using the exifread library.

---

##  What It Does

- Opens a .jpg image file
- Extracts metadata like:
  - Camera make & model
  - Image resolution
  - Date taken
  - GPS info (if available)
- Displays the metadata in the terminal

---

##  Requirements

- Python 3.x
- exifread module

- ## 🧪 Troubleshooting Guide

If your EXIF metadata viewer returns *"No EXIF metadata found."*, here are a few possible causes and how to fix them:

---

###  1. Image Has No EXIF Data

*Cause:*  
Some images (e.g., screenshots, edited photos, or downloaded from websites) may have EXIF metadata stripped out.

*Fix:*  
Use an unedited image taken directly from a smartphone or DSLR camera.

*Example:*  
Take a photo using your phone, rename it to sample1.jpg, and try again.

---

###  2. Wrong File Path

*Cause:*  
The image file is not in the same directory as the Python script.

*Fix:*  
- Make sure sample1.jpg is in the *same folder* as your .py script.
- Or use an *absolute path*:
  ```python
  with open("C:/Users/YourName/Desktop/sample1.jpg", "rb") as file:
