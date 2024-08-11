import speech_recognition as sr
import time

def getText():
    recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer
    
    with sr.Microphone() as source:
        print("in ascolto")
        audio = recognizer_instance.listen(source)  # snowboy configuration protrebbe aiutarmi
        print("Fine ascolto")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        print(text)
    except Exception:
        text = ""
    return text



