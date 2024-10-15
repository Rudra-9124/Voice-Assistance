import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("alex","")
        query = query.replace("google search","")
        query = query.replace("google","")
        query = query.replace("who is","")
        query = query.replace("what is","")
        speak("This is what I Found on google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "play" in query:
        speak("This is what I found for your search!")
        song = query.replace('play',"")
        speak("playing" + song)
        pywhatkit.playonyt(song)

def searchWikipidea(query):
    if "wikipidea" in query:
        speak("Searching from wikipidea...")
        query = query.replace("wikipidea","")
        query = query.replace("search wikipidea","")
        query = query.replace("alex","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipidea..")
        print(results)
        speak(results) 
















    