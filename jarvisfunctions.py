#modules used

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


#for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))



#engine for speak function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)





#speak function make program to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#this function wish user
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning BOSS")
    elif hour>=12 and hour < 18:
        speak("good Afternoon BOSS")
    else:
        speak("Good Evening BOSS ")
    speak("I am your assistant, how may i help you")


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
        speak("i am not getting you...., please speak Again")
        return "None"
    return query


#This function send mail
def sendEmail(email, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhanupartapsingh21@gmail.com', 'yuioplkj0011')
    server.sendmail('bhanupartapsingh21@gmail.com', email, content)
    server.close()


#This function changes brightness of screen in windows
def change_brightness():
    brightness=takecommand()
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)
    speak("Is it Good now")
    answer=takecommand()
    if answer=='yes'or answer=='thankyou':
        speak("I am glad that i help you, BOSS,Enjoy")
        continue
    elif answer == "no":
        speak("is it high or low")
        answer2=takecommand()
        if answer2=="high":
            brightnes=brightness-10
            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)

        elif answer2 == "low":
            brightness=briightness+10
            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)


#This function is to change System volume
def change_volume()
    speak("Do u want to increase volume. just say Yes, No or Max")
    a = takecommand()
    if a='yes' or a=='Yes':
        volume.SetMasterVolumeLevel(-5.0, None)
    elif a=='no' or a=='No':
        speak("Do want to decrease volume")
        b=takecommand()
        if b=='yes' or b=='Yes':
            volume.SetMasterVolumeLevel(-15.0, None)
                        
        elif b=='no' or b=='No':
            continue
        elif a=='Max' or a=='max':
            volume.SetMasterVolumeLevel(-0.0, None)

#This function is to Mute system sounds
def mute_volume():
    volume.SetMasterVolumeLevel(-50.0, None)
