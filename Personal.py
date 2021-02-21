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
import win32com.client as wincl
import ctypes
from twilio.rest import Client
from wolframalpha import Client
import json
from urllib.request import urlopen
import requests
import smtplib
import pyjokes
import operator
from bs4 import BeautifulSoup
import operator
import PyPDF2
from tkinter.filedialog import *


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
        try:
            speak("Searching Wikepedia...")
            query=query.replace("wikepedia","")
            result=wikipedia.summary(query,sentences=1) #return 2 sentence
            speak("According to Wikipedia")
            speak(result)
        except Exception as e:
            speak("An error occured, try again")
    elif 'open youtube' in query:
        try:
            webbrowser.open("youtube.com")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open whatsapp' in query:
        try:
            webbrowser.open("https://web.whatsapp.com/")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open google' in query:
        try:
            webbrowser.open("google.com")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open stackoverflow' in query:
        try:
            webbrowser.open("stackoverflow.com")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open wiki' in query:
        try:
            webbrowser.open("https://en.wikipedia.org/wiki/Wikipedia")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open chandigarh university site' in query:
        try:
            webbrowser.open("https://uims.cuchd.in/uims/")
        except Exception as e:
            speak("An error occured, try again")
    elif 'play music' in query:
        try:
            musid_dir='F:\\video songs'  #\\ to escape character
            songs=os.listdir(musid_dir)
            print(songs)
            os.startfile(os.path.join(musid_dir,random.choice(songs)))

        except Exception as e:
            speak("An error occured, try again")
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'open my project folder' in query:
        try:
            projectPath="E:\\Project2"
            os.startfile(projectPath)
        except Exception as e:
            speak("An error occured, try again")
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
            speak("Sorry your mail is not able to send")
    elif 'thank you' in query:
        speak("Your most welcome sir!")
    elif 'open notepad' in query:
        speak("Opening notepad sir!")
        try:
            os.system("Notepad")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open chrome' in query:
        speak("Opening chrome sir!")
        try:
            os.system("chrome")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open vlc player' in query:
        speak("Opening vlc sir!")
        try:
            os.system("VLC")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open telegram' in query:
        speak("Opening telegram sir!")
        try:
            os.system("telegram")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open excel' in query:
        speak("Opening excel sir!")
        try:
            os.system("excel")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open word' in query:
        speak("Opening word sir!")
        try:
            os.system("winword")
        except Exception as e:
            speak("An error occured, try again")
    elif 'open calc' in query:
        speak("Opening calculator sir!")
        try:
            os.system("calc")
        except Exception as e:
            speak("An error occured, try again")
    elif "restart" in query:
        try:
            subprocess.call(["shutdown", "/r"])
        except Exception as e:
            speak("An error occured, try again")

    elif "hibernate" in query or "sleep" in query:
        try:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        except Exception as e:
            speak("An error occured, try again")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        try:
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        except Exception as e:
            speak("An error occured, try again")
    elif "write a note" in query:
        speak("What should i write, sir")
        note = takeCommand()
        try:
            file = open('text.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            elif 'no' in snfm:
                file.write(note)
        except Exception as e:
            speak("An error occured, try again")

    elif "open note" in query:
        try:
            speak("Showing Notes")
            file = open("text.txt", "r")
            print(file.read())
            speak(file.read(6))
        except Exception as e:
            speak("An error occured, try again")

    elif "where is" in query:
        try:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/dir//" + location + "")
        except Exception as e:
            speak("An error occured, try again")
    elif "don't listen" in query or "stop listening" in query:
        try:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        except Exception as e:
            speak("An error occured, try again")
    elif 'lock window' in query:
        try:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        except Exception as e:
            speak("An error occured, try again")

    elif 'shutdown system' in query:
        try:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        except Exception as e:
            speak("An error occured, try again")
    elif 'open this pc' in query:
        try:
            speak("This pc opening")
            os.system("thispc")
        except Exception as e:
            speak("An error occured, try again")
    elif "local disk c" in query:
        try:
            speak("Local disk C opening sir!")
            os.startfile("C:")
            os.scandir()
            speak("Folder name sir.")
            C=takeCommand()
            if "folder" in C:
                speak("Speak folder name")
                folInC=takeCommand()
                webbrowser.open("C:/"+folInC)
        except Exception as e:
            speak("An error occured, try again")
    elif "are you listening me" in query:
        speak("Yes sir!")

    elif "local disk d" in query:
        try:
            speak("Local disk D opening sir!")
            os.startfile("D:")
            os.scandir()
            speak("Folder name sir.")
            D=takeCommand()
            if "folder" in D:
                speak("Speak folder name")
                folInD=takeCommand()
                webbrowser.open("D:/"+folInD)
        except Exception as e:
            speak("An error occured, try again")
    elif "local disk e" in query:
        try:
            speak("Local disk E opening sir!")
            os.startfile("E:")
            os.scandir()
            speak("Folder name sir.")
            E=takeCommand()
            if "folder" in E:
                speak("Speak folder name")
                folInE=takeCommand()
                webbrowser.open("E:/"+folInE)
        except Exception as e:
            speak("An error occured, try again")
    elif "local disk f" in query or "local disc f" in query:
        try:
            speak("Local disk F opening sir!")
            os.startfile("F:")
            os.scandir()
            speak("Folder name sir.")
            F=takeCommand()
            if "folder" in F:
                speak("Speak folder name")
                folInF=takeCommand()
                name=folInF
                file1=open(name+".txt", "r")
                print(file1.read())
                speak(file1.read(6))
        except Exception as e:
            speak("An error occured, try again")

    elif "make a call" in query:
        try:
            speak("Calling system opening!")
            account=os.environ["AC918bfb12ad92b2fbf42b2c8f33b60817"]
            auth_token=os.environ["70af4bcc9734c5fa17af27f793274b1f"]
            client=Client(account,auth_token)
            speak("Sir whom to call!")
            thisdict1 = {
                "Priyanshu Singh": "+916388016659",
                "Sagar Kumar": "+919876233807"
            }
            content2 = takeCommand()
            call=client.calls.create(
                to="+916388016659",
                from_=thisdict1[content2],
                url="http://demo.twilio.com/docs/voice.xml"
            )
            print(call.sid)
        except Exception as e:
            speak("An error occured, try again")
    elif 'news' in query:
        try:
            jsonObj = urlopen('''http://newsapi.org/v2/everything?q=tesla&from=2021-01-21&sortBy=publishedAt&apiKey=e2c99b9641f746f98088eb727842c6cd''')
            data = json.load(jsonObj)
            i = 1
            speak('here are some top news from the times of india')
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                if i==10:
                    break
                i += 1
        except Exception as e:
            speak("Check your network connection?")

    elif 'temperature' in query:
        try:
            search="Delhi"
            url=f"https://www.google.com/search?q=temperature+in+{search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f" current temprature in {search} is {temp}")
        except Exception as e:
            speak("An error occured, try again")

    elif 'jokes' in query:
        try:
            list_of_jokes = pyjokes.get_jokes(language="en", category="all")
            for i in range(0, 4):
                speak(list_of_jokes[i])
        except Exception as e:
            speak("An error occured, try again")
    elif 'pdf reader' in query:
        try:
            book=askopenfilename()
            pdfreader=PyPDF2.PdfFileReader(book)
            pages=pdfreader.numPages
            for num in range(0,pages):
                page=pdfreader.getPage(num)
                text=page.extractText()
                player= pyttsx3.init()
                player.say(text)
                player.runAndWait()
        except Exception as e:
            speak("An error occured, try again")


    elif "calculate" in query:
        try:
            speak("Enter the operation and number")
            my_string = takeCommand()
            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truediv__,
                    'Mod': operator.mod,
                    'mod': operator.mod,
                    '^': operator.xor,
                }[op]


            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            print(eval_binary_expr(*(my_string.split())))
            speak(f"Your result is {eval_binary_expr(*(my_string.split()))}")
        except Exception as e:
            speak("An error occured, try again")
    elif 'empty recycle bin' in query:
        try:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        except Exception as e:
            speak("An error occured, try again")
    elif "what is" in query or "who is" in query:
        speak("Answer in process.")
        client = wolframalpha.Client("L3VYUJ-4JWGQ64HW9")
        res = client.query(query)
        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")
    elif 'quit' in query or 'close assistant' in query:
        speak("Closing sir!")
        os.system("Exiting")
        break
    elif "whatsapp" in query:
        try:
            speak("Whatsapp opening!")
            webbrowser.open("https://web.whatsapp.com/")
        except Exception as e:
            speak("An error occured, try again")
    elif "change name" in query:
        speak("What would you like to call me, Sir ")
        assname = takeCommand()
        speak("Thanks for naming me")
    elif "youtube search" in query:
        speak("What do you want to search?")
        ytube=takeCommand()
        speak(ytube)
        try:
            webbrowser.open(f'https://www.youtube.com/results?search_query='+ytube+"")
        except Exception as e:
            speak("An error occured, try again")
    elif "linkedin" in query:
        try:
            webbrowser.open("https://in.linkedin.com/")
        except Exception as e:
            speak("An error occured, try again")
    elif "black board" in query or "bb" in query:
        try:
            webbrowser.open("https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fcourse")
        except Exception as e:
            speak("An error occured, try again")

    elif "git" in query or "github" in query:
        try:
            webbrowser.open("https://github.com/")
        except Exception as e:
            speak("An error occured, try again")

    elif "what's your name" in query or "What is your name" in query:
        try:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        except Exception as e:
            speak("An error occured, try again")
    else:
        speak("Speak again!")
