import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source)

    try:
        print("recognising....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        return "None"
    return query

while True:
    query = takeCommand().lower()    
    if 'hey friday' or 'Friday uth jao' or 'Friday chalo kaam pe Lag Jao' or 'bhut soo liye' in query:
        path="FRIDAY.py"
        os.startfile(path)
        exit()
    
