#modules used
from __future__ import print_function
import psutil
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
import wmi

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
        speak("good morning..BOSS")
    elif hour>=12 and hour < 18:
        speak("good Afternoon..BOSS")
    else:
        speak("Good Evening..BOSS ")
    speak(".  I  am  your  assistant")
    speak("HOW  May  i  help  you")


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
    server.login('s.a.bkpr091@gmail.com', 'Akanksha1221')
    server.sendmail('s.a.bkpr091@gmail.com', email, content)
    server.close()


#This function changes brightness of screen in windows
def change_brightness(level):
    brightness=level
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)
    speak("Is it Good now")
    answer=takeCommand()
    if answer=='yes'or answer=='thankyou':
        speak("I am glad that i help you, BOSS,Enjoy")
        
    elif answer == "no":
        speak("Do you want Increase It Or decrease It")
        answer2=takeCommand()
        if answer2=="increase":
            brightnes=brightness+10
            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)

        elif answer2 == "decrease":
            brightness=briightness-10
            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)

#This Functions Converts seconds into hours and minutes and return it  
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d Hours: %02d ,Minutes" % (hh,mm)

#This Function check battery of device

def power_Check():
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        return sys.exit("no battery is installed")

    print("charge:     %s%%" % round(batt.percent, 2))
    speak("Battery left:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print("status:     %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        print("plugged in: yes")
        speak("status:     %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        speak("plugged in: yes")
    else:
        print("left:       %s" % secs2hours(batt.secsleft))
        print("status:     %s" % "discharging")
        print("plugged in: no")
        speak("battery time left:       %s" % secs2hours(batt.secsleft))
        speak("status:     %s" % "Discharging")
        speak("Charger Not detected")
        if batt.percent < 20:
            speak("Connect Power Supply... to keep going ON")
        



#This function is to change System volume
def change_volume():
    speak("Do u want to increase volume. just say Yes, No,  Max")
    a = takeCommand()
    if a=='yes' or a=='Yes':
        volume.SetMasterVolumeLevel(-5.0, None)
    elif a=='Max' or a=='max':
            volume.SetMasterVolumeLevel(-0.0, None)

    elif a=='no' or a=='No':
        speak("Do want to decrease volume")
        b=takeCommand()
        if b=='yes' or b=='Yes':
            volume.SetMasterVolumeLevel(-15.0, None)
                        
        elif b=='no' or b=='No':
            return 0

#This function is to Mute system sounds
def mute_volume():
    volume.SetMasterVolumeLevel(-50.0, None)

def wiki(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except :
        print("Nothing available... Sorry")
        speak("Nothing available... Sorry")
                
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if  query=="what is your name":
                speak("My name is FRIDAY")
                speak("I am your friend")
                speak(" Tell me What to do")

        elif query=="mute":
                speak("Muting")
                mute_volume()

                
        elif 'friday' in query:
            query=query.replace("Friday ","")
        
            
            if 'search wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("search wikipedia", "")
                wiki(query)

           
            elif 'open youtube' in query:
                speak('OK BOSS ,opening youtube')
                webbrowser.open('www.youtube.com')

            

            elif "open shareit" in query:
                speak("ok Boss , opening shareit")
                codepath="C:\\Program Files (x86)\\SHAREit Technologies\\SHAREit\\SHAREit.exe"
                os.startfile(codepath)

            elif "open chrome" in query:
                speak("Ok Boss,Opening Chrome")
                codepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codepath)

            elif  "take student detail" in query:
                codepath="student details.py"
                os.startfile(codepath)

            elif "send mail" in query:
                try:
                    speak("What Should i say?")
                    content = takeCommand()
                    speak("To Whom")
                    email=input("Please enter mail id manually")
                    sendEmail(email, content)
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif"restart yourself" in query:
                speak("Maybe error will solved")
                os.startfile("FRIDAY.py")
                exit()
            
            elif "shutdown" in query:
                os.system("shutdown.bat")

            elif "restart" in query:
                os.system("restart.bat")

            elif "hibernate" in query:
                os.system("hibernate.bat")

            

            elif "Unmute sound" in query:
                speak("Ok boss")
                volume.SetMasterVolumeLevel(-10.0, None)
                speak("Do u want to increase volume. just say Yes, No or Max")
                a = takecommand()

                if a=='yes' or a=='Yes':
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

            elif query =="audio service stop":
                print("stoping Audio Services")
                speak("stoping Audio Services")
                os.system("mute.lnk")

            elif"change volume" in query:
                change_volume()


            elif "change brightness" in query:
                query=query.replace("change brightness to ","")
                if "full" or "Max"in query:
                    level=int(100)
                else:
                    level=int(query)
                if level > 100:
                    level=level-100
                change_brightness(level)


            elif "battery status" in query:
                power_Check()
                
            elif "wireless connection disable" in query:
                os.system("admin_wifi_disable.lnk")
                
            elif "wireless connection enable" in query:
                os.system("admin_wifi_enable.lnk")

        

            elif query=="time":
                a=datetime.datetime.now().strftime("%H:%M:%S")
                print(a)
                b=datetime.datetime.now().strftime("%H Hours:%M Minutes")
                speak(f"Sir Time is {b}")

            elif query=="exit" or query=="sleep jarvis" or query=="goodbye" :
                speak("GoodBye..BOSS")
                speak("Call me In Need")
                exit()

            elif 'copy files' in query:
                os.startfile("copy_files_only.py")

            elif 'move files' in query:
                os.startfile("move_files_only.py")



    



            elif query=="":
                print("Yes Tell me What to do")
                speak("Yes Tell me What to do")

            else:
                speak("Sorry")
                speak(" their is no code for ")
                speak(query)
