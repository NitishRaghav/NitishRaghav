from os import path
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

d={}
sec=int(datetime.datetime.now().second)
nameee="detail_%d.txt"%(sec)
file=open(nameee,'w')
def getdata():
    d['name']=input("Enter your name\n")
    d['class']=input("Enter your class\n")
    d['age']=input("Enter your age\n")
    d['sch_name']=input("Enter your school name \n")
    d['phn_num']=input("Enter your phone number\n")

def voicegetdata():
    d['name']=takeCommand()
    d['class']=takeCommand()
    d['age']=takeCommand()
    d['sch_name']=takeCommand()
    d['phn_num']=takeCommand()

def save():
    file.write("Name is : "+d['name']+"\n")
    file.write("Class is : "+d['class']+"\n")
    file.write("Age is : "+d['age']+"\n")
    file.write("Your school name : "+d['sch_name']+"\n")
    file.write("Phone number is : "+d['phn_num']+"\n")

    file.write("\n")

if __name__=="__main__":
    a=input(" press 1 to go with voice\n press any key if you prefer Typing ")
    if a=='1':
        voicegetdata()
    else:
        getdata()
    while True:
        if a=='1':
            speak("Name : " + d['name'] + "\n"+ "Class is : " +d['class']+"\n"+ "Age is : "+d['age']+"\n"+"School name is : "+d['sch_name']+"\n"+"Your phone number is : "+d['phn_num']+"\n")
        else:    
            print("Name : " + d['name'] + "\n"+ "Class is : " +d['class']+"\n"+ "Age is : "+d['age']+"\n"+"School name is : "+d['sch_name']+"\n"+"Your phone number is : "+d['phn_num']+"\n")
        a=input("If above imformation is Correct press Y \n press N if not")
        if a=='Y' or a=='y':
            print("Thanks for the confirmation\n")
            save()
            b=input("New Student ?\nY or N")
            if b=='Y' or b=='y':
                if a=='1':
                   voicegetdata()     
                else:
                    getdata()
            else:
                file.close()
                exit()
        else:
            print("Please enter again\n")

            if a=='1':
                voicegetdata()
            else:
                getdata()

