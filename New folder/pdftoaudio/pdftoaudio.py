# pip install pyttsx3
# pip install PyPDF2

import pyttsx3
import PyPDF2   

# path of the PDF file
path = open('python.PDF', 'rb')

# creating a pdf file reader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page which you want to start to read
from_page = pdfReader.getPage(12)

# extracting the text from the pdf file
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
