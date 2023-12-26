from PIL import Image
import glob
import os
import pyperclip
import pytesseract
import tkinter as tk



# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

list_of_files = glob.glob(r'C:\\Users\\milad\\Pictures\\ocr\\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

text = pytesseract.image_to_string(latest_file)

# Simple image to string
pyperclip.copy(text)

# window = tk.Tk()
# window.title = 'OCR Text'
# toplevel = tk.Toplevel(window)
# toplevel.title = 'Top Level'
# window.mainloop()

# print()

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('test.png'))

# List of available languages
# print(pytesseract.get_languages(config=''))

# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
# try:
    # print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
    # print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
# except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    # pass

# Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.png')))

# Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.png')))

# Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.png')))

# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
# with open('test.pdf', 'w+b') as f:
    # f.write(pdf) # pdf type is bytes by default

# Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

# Get ALTO XML output
# xml = pytesseract.image_to_alto_xml('test.png')