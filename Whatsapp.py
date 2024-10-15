import pyttsx3
import pywhatkit
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said: {query} \n")
    except Exception as e:
        print("Say that Again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
upadte = int((datetime.now()+timedelta(minutes=1.5)).strftime("%M"))

def sendMessage():
    speak("who do you wnat to message?")
    a = int(input('''Tirth - 1  Darsh - 2   Ansh - 3'''+"\n"))
    if a == 1:
        speak("Whats the message")
        msg = str(input("Enter message :"))
        pywhatkit.sendwhatmsg("+919664911845",msg,time_hour=strTime,time_min=upadte)
    elif a==2:
        speak("Whats the message")
        msg = str(input("Enter message :"))
        pywhatkit.sendwhatmsg("+918155838121",msg,time_hour=strTime,time_min=upadte)
    elif a==3:
        speak("Whats the message")
        msg = str(input("Enter message :"))
        pywhatkit.sendwhatmsg("+919099149405",msg,time_hour=strTime,time_min=upadte)


    