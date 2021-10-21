import pyttsx3
from pyttsx3 import engine
import PyPDF2
def speak(text):
    engine= pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
book_name=open('think.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book_name)
pages=pdfReader.numPages
print(pages)
page=pdfReader.getPage(18)
book=page.extractText()
speak(book)