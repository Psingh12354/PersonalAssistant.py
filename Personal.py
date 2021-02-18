import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import winshell
import subprocess
import wolframalpha
import time
import ctypes
import json
from urllib.request import urlopen
import requests
import smtplib
import pyjokes
import operator
from ecapture import ecapture as ec
engine=pyttsx3.init("sapi5") #sapi5 microsoft speech api
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id) #0 for male 1 for female
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening!")
    speak("I am your Personal Assistant Sir.")
    speak("Tell me how i can help you.")

def takeCommand():
    #it take user input
    r=sr.Recognizer() #recognize sound
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1 #how your voice should be listen
        audio=r.listen(source)
    try:
        print("Recognizing...") #in case of error
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pythonp558@gmail.com','python900')
    server.sendmail('pythonp558@gmail.com',to,content)

#wishMe()
while True:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching Wikepedia...")
        query=query.replace("wikepedia","")
        result=wikipedia.summary(query,sentences=1) #return 2 sentence
        speak("According to Wikipedia")
        print(result)
        speak(result)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'open wiki' in query:
        webbrowser.open("https://en.wikipedia.org/wiki/Wikipedia")
    elif 'open chandigarh university site' in query:
        webbrowser.open("https://uims.cuchd.in/uims/")
    elif 'play music' in query:
        musid_dir='F:\\video songs'  #\\ to escape character
        songs=os.listdir(musid_dir)
        print(songs)
        os.startfile(os.path.join(musid_dir,random.choice(songs)))
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open my project folder' in query:
        projectPath="E:\\Project2"
        os.startfile(projectPath)
    elif 'send email' in query:
        try:
            speak("Sir whom to send!")
            thisdict = {
                "Priyanshu Singh": "priyanshu.7068183126@gmail.com",
                "Sagar Kumar": "sagarkumsrdotcom3@gmail.com"
            }
            content1 = takeCommand()
            speak("What should I say?")
            to=thisdict[content1]
            content=takeCommand()
            sendEmail(to,content)
            speak("Email has beed sent!")
        except Exception as e:
            print(e)
            speak("Sorry your mail is not able to send")
    elif 'thank you' in query:
        speak("Your most welcome sir!")
    elif 'open notepad' in query:
        speak("Opening notepad sir!")
        os.system("Notepad")
    elif 'open chrome' in query:
        speak("Opening chrome sir!")
        os.system("chrome")
    elif 'open vlc player' in query:
        speak("Opening vlc sir!")
        os.system("VLC")
    elif 'open telegram' in query:
        speak("Opening telegram sir!")
        os.system("telegram")
    elif 'open excel' in query:
        speak("Opening excel sir!")
        os.system("excel")
    elif 'open word' in query:
        speak("Opening word sir!")
        os.system("winword")
    elif 'open calc' in query:
        speak("Opening calculator sir!")
        os.system("calc")
    elif 'add number' in query:
        speak("What's the number?")
        speak("First number sir.")
        num1=takeCommand()
        speak("Second number sir.")
        num2=takeCommand()
        speak(sum(int(num1),int(num2)))
    elif 'subtract number' in query:
        speak("What's the number?")
        speak("First number sir.")
        num1=takeCommand()
        speak("Second number sir.")
        num2=takeCommand()
        speak(int(num1)-int(num2))
    elif 'multiply number' in query:
        speak("What's the number?")
        speak("First number sir.")
        num1=takeCommand()
        speak("Second number sir.")
        num2=takeCommand()
        speak(int(num1)*int(num2))
    elif 'divide number' in query:
        speak("What's the number?")
        speak("First number sir.")
        num1=takeCommand()
        speak("Second number sir.")
        num2=takeCommand()
        speak(int(num1)/int(num2))
    elif 'modulus of number' in query:
        speak("What's the number?")
        speak("First number sir.")
        num1=takeCommand()
        speak("Second number sir.")
        num2=takeCommand()
        speak(int(num1)%int(num2))
    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "Jarvis Camera ", "img.jpg")

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])
    elif "write a note" in query:
        speak("What should i write, sir")
        note = takeCommand()
        file = open('text.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = takeCommand()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show note" in query:
        speak("Showing Notes")
        file = open("text.txt", "r")
        print(file.read())
        speak(file.read(6))
    elif "weather" in query:

        # Google Open weather website
        # to get API of Open weather
        api_key = "Api key"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        speak(" City name ")
        print("City name : ")
        city_name = takeCommand()
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
                weather_description))

        else:
            speak(" City Not Found ")

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.nl / maps / place/" + location + "")
    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop jarvis from listening commands")
        a = int(takeCommand())
        time.sleep(a)
        print(a)
    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
    elif 'news' in query:

        try:
            jsonObj = urlopen(
                '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
            data = json.load(jsonObj)
            i = 1

            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:

            print(str(e))
    elif "what is" in query or "who is" in query:

        # Use the same API key
        # that we have generated earlier
        client = wolframalpha.Client("API_ID")
        res = client.query(query)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")
    elif 'quit' in query:
        speak("Closing sir!")
        os.system("Exiting")
        break
