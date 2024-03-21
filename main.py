# let's create a pdf to audio convertor 
# for this we need some labiry to install that is //pip install// "pyttsx3, pdfplumber, pyPDF2"
# let's import it these labiry
import pyttsx3
import pdfplumber
import PyPDF2

# Appload the pdf 
file = 'Abook.pdf'
# create a pdf file object
pdfFileObj = open(file, 'rb')
# Create a file reader object 
pdf_reader = PyPDF2.PdfReader(pdfFileObj)
# Get the number of pdf pages
pages = len(pdf_reader.pages)
# Create a plumber object and loop thourgh the pages
with pdfplumber.open(file) as pdf:
    # loop thourgh the page number
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()


