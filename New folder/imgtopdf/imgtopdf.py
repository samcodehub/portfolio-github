# pip install img2pdf

import img2pdf
from PIL import Image

# storing image path 
img_path = "Image.jpg"

# storing pdf path
pdf_path = "pdf.pdf"

# opening image file
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output 
print("Successfully made pdf file")
