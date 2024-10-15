import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestNews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=16b63a5fce1c4400b7ea35cdb498b2f2",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=16b63a5fce1c4400b7ea35cdb498b2f2",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=16b63a5fce1c4400b7ea35cdb498b2f2",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=16b63a5fce1c4400b7ea35cdb498b2f2",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=16b63a5fce1c4400b7ea35cdb498b2f2",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=16b63a5fce1c4400b7ea35cdb498b2f2"}
    content = None
    url = None
    print("Which field news do you want, [Business], [Entertainment], [Health], [Science], [technology], [Sports]")
    speak("Which field news do you want, [Business], [Entertainment], [Health], [Science], [technology], [Sports]")
    field = input("Enter field of news that you want:")
    for key,value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url=True
    if url is True:
        print("url not found")
        speak("url not found")
    
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print("for more info visit: "+news_url)

        a=input("Press 1 to continue and Press 2 to stop ")
        if str(a)=="1":
            pass
        elif str(a)=="2":
            break

    speak("thats all")
