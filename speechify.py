# pyttsx3 is a text-to-speech conversion library in python
import pyttsx3
# PyPDF2 a python library capable of transforming pdf files
from PyPDF2 import PdfReader

# add path for the directory containing our pdf 
pdfreader = PdfReader(open('/home/murage/Documents/comp420.pdf', 'rb'))
engine = pyttsx3.init()
number_of_pages = len(pdfreader.pages)
for page in range(number_of_pages):
    text = pdfreader.getPage(page).extract_text()
    legible_text = text.strip().replace('\n',' ')
    print(f"{legible_text}")
    engine.say(legible_text)
    engine.save_to_file(legible_text, 'file.mp3')
    engine.runAndWait()
engine.stop()


