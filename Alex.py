import pyttsx3
import speech_recognition
import requests
import datetime
import os
from bs4 import BeautifulSoup
import pyautogui
import random
import webbrowser
import pyautogui
import speedtest
import time

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
        print("🎤 Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 500
        audio = r.listen(source,0,4)
    try:
        print("🧠 Understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"🗣️ You Said: {query} \n")
    except Exception as e:
        print("🔊 Say that Again \n")
        return "None"
    return query

if __name__ == "__main__":
    while(True):
        query = takeCommand().lower()
        if "hello" in query:
            from Greetme import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok, you can call me anytime")
                    break
                    
            # ============ Translate ============
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("alex","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "hello" in query:
                    speak("Hello! How are you?")
                elif "i am fine" in query:
                    speak("That's Great")
                elif "what is your name" in query:
                    speak("My name is Alex and I am here to assist you.")
                elif "who is alex" in query:
                    speak("my name is Alex and I am your ChatBot.")
                elif "what is your birth date" in query:
                    speak("I born on 1 March 2024.")
                elif "how are you" in query:
                    speak("I am fine")
                elif "thank you" in query:
                    speak("You are Welcome, Sir")

            # ============ Internet Speed ============
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_speed = round(wifi.upload()/1048576, 2)  #Megabyte = 1024*1024 Bytes
                    download_speed = round(wifi.download()/1048576, 2)
                    print(f"Upload Speed : {upload_speed}")
                    speak(f"upload speed is {upload_speed}")
                    print(f"Download Speed : {download_speed}")
                    speak(f"Download Speed is {download_speed}")

            # ============ Google/Youtube/Wikipedia ============
                elif "google" in query:
                    from SearchNow import searchGoogle
                    speak("Searching in Google")
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    speak("Searching on Youtube")
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipidea
                    speak("Searching Wikipedia")
                    searchWikipidea(query)

            # ============ Media Controls ============
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from Keyboard import volumeUp
                    speak("Turning Volume Up")
                    volumeUp()
                elif "volume down" in query:
                    speak("Turning Volume Down")
                    from Keyboard import volumeDown
                    volumeDown()

            # ============ Calculate ============
                elif "calculate" in query:
                    from Calculate import WolfRamAlpha
                    from Calculate import calc
                    query = query.replace("alex","")
                    query = query.replace("calculate","")
                    calc(query)

            # ============ Playlist ============
                elif "playlist" in query:
                    speak("Playing your favorite songs")
                    a = (1,2,3,4,5)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=ciLGHX_mq48")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=muds1gFUTN8")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=z-PUf6k552I")
                    elif b==4:
                        webbrowser.open("https://www.youtube.com/watch?v=jabs2RM7Tqo")
                    elif b==5:
                        webbrowser.open("https://www.youtube.com/watch?v=jrOIZA-G-z4")

            # ============ News ============
                elif "live news" in query:
                    print("Which News Channel do you want to watch, [Aaj Tak], [ABP], [News24]")
                    speak("Which News Channel do you want to watch, [Aaj Tak], [ABP], [News24]")
                    while True:
                        ch = takeCommand().lower()
                        if ch == "news24" or ch == "aaj tak" or ch == "abp":
                            break
                        else:
                            speak("Select valid channel")
                    speak("Opening live news")
                    if "aaj tak" in ch:
                        webbrowser.open("https://www.youtube.com/watch?v=Nq2wYlWFucg")
                    elif "abp" in ch:
                        webbrowser.open("https://www.youtube.com/watch?v=DgLtz4UHqPk")
                    elif "news24" in ch:
                        webbrowser.open("https://www.youtube.com/watch?v=RH5iZc5Rglc")

                elif "news" in query:
                    from NewsRead import latestNews
                    latestNews()

            # ============ Opening Apps ============
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("alex","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(3)
                    pyautogui.press("enter")

            # ============ Temperature ============
                elif "temperature" in query:
                    search = "temperature in ahmedabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "weather" in query:
                    search = "temperature in ahmedabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

            # ============ Time ============
                elif "time" in query:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    speak('Current time is '+time)

            # ============ Remember ============
                elif "remember that" in query:
                    remembermsg = query.replace("remember that","")
                    remembermsg = query.replace("alex","")
                    speak("You told me to "+remembermsg)
                    remember = open("Remember.txt","w+")
                    remember.write(remembermsg)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt")
                    speak("You told me to "+remember.read())

            # ============ Screenshot ============
                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

            # ============ Photo Clicking ============
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(5)
                    speak("smile")
                    pyautogui.press("enter")

            # ============ Whatsapp ============
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                elif "bye" in query:
                    speak("Goodbye to you too.")
                    exit()
                    
            # ============ Shutdown ============
                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown?")
                    ans = input("Do you wish to shutdown the system? (yes or no): ")
                    if ans=="yes":
                        os.system("shutdown /s /t 1")
                    elif ans=="no":
                        speak("Shutdown Aborted")

            # ============ Restart ============
                elif "restart system" in query:
                    speak("Are you sure you want to shutdown?")
                    ans = input("Do you wish to shutdown the system? (yes or no): ")
                    if ans=="yes":
                        os.system("shutdown /r /t 1")
                    elif ans=="no":
                        speak("Restart Aborted")
        