<h1 align=center><b>PersonalAssistant.py</b></h1>

### Images
![](https://github.com/Psingh12354/PersonalAssistant.py/blob/main/front.PNG)
![](https://github.com/Psingh12354/PersonalAssistant.py/blob/main/file.PNG)
![](https://github.com/Psingh12354/PersonalAssistant.py/blob/main/personal.PNG)
![](https://github.com/Psingh12354/PersonalAssistant.py/blob/main/hist.PNG)
### Code
```
import argparse
import ctypes
import datetime
import datetime
import json
import operator
import operator
import os
import re
import os.path
import phonenumbers
import email
import folium
import imaplib
from phonenumbers import geocoder
import traceback
import random
from phonenumbers import carrier
import shutil
import smtplib
import mechanize
import socket
import news_module
import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile
import subprocess
import time
import psutil
import webbrowser
import wmi
import platform
import winsound
from datetime import date
from tkinter.filedialog import *
from urllib.request import urlopen

import PyPDF2
import cv2
import numpy as np
import pyautogui
import pyjokes
import pyttsx3
import requests
import sounddevice as sd
import speech_recognition as sr
import wikipedia
import win32com.client as wincl
import winshell
import wolframalpha
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup
from googlesearch import search
from scipy.io.wavfile import write
from scipy.io.wavfile import write
from selenium import webdriver
from twilio.rest import Client
from wolframalpha import Client
from word2number import w2n
from ipregistry import IpregistryClient
from geopy.geocoders import Nominatim
import geopy
#webbrowser.open("E://Project2//AudioH//index.html")

#location
resul = requests.get('https://ipinfo.io/')
data=resul.json()
city=data['city']
# import geocoder
# g = geocoder.ip('me')
# print(g.latlng)
# from ipregistry import IpregistryClient
# client = IpregistryClient("tryout")
# ipInfo = client.lookup()
# print(ipInfo)
# import winrt.windows.foundation as wf
# u = wf.Uri("https://github.com/")
# u2 = u.combine_uri("Microsoft/xlang/tree/master/src/tool/python")
# print(str(u2))


#----

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
    if not os.path.exists('History'):
        os.makedirs('History')
    list_of_file = os.listdir("History")
    file3 = open("History//history.txt", "a+")
    save_time=datetime.datetime.now().strftime("\n%H:%M:%S")
    file3.write(save_time)
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1 #how your voice should be listen
        audio=r.listen(source,phrase_time_limit=8)
    try:
        print("Recognizing...") #in case of error
        file3.write("\nRecognizing...\n")
        query=r.recognize_google(audio,language='en-in')
        file3.write(f"User said: {query}")
        print(f"User said: {query}")
    except Exception as e:
        #print(e)
        file3.write("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your Email','Your email pwd')
    server.sendmail('your Email',to,content)

wishMe()
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
        if not os.path.exists('Gmail_History'):
            os.makedirs('Gmail_History')
        list_of_file = os.listdir("Gmail_History")
        file4 = open("Gmail_History//gmail.txt", "a+")
        save_time = datetime.datetime.now().strftime("\n%H:%M:%S\n")
        file4.write(save_time)
        try:
            speak("Sir whom to send!")
            thisdict = {
                "Sender1 name": "Sender 1 Email",
                "Sender2 name": "Sender 2 Email"
            }
            phrase_time_limit = 60
            content1 = takeCommand()
            file4.write(content1+"\n")
            print(content1)
            speak("What should I say?")
            to=thisdict[content1]
            file4.write(to + "\n")
            content=takeCommand()
            file4.write(content+"\n")
            sendEmail(to,content)
            speak("Email has beed sent!")
        except Exception as e:
            file4.write( "Sorry your mail is not able to send"+ "\n")
            speak("Sorry your mail is not able to send")
    elif "read email" in query or "check latest email" in query or "check my mail" in query:
        try:
            ORG_EMAIL = "@gmail.com"
            FROM_EMAIL = "EmailFirst name till @" + ORG_EMAIL
            FROM_PWD = "python900"
            SMTP_SERVER = "imap.gmail.com"
            SMTP_PORT = 993
            def read_email_from_gmail():
                try:
                    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
                    mail.login(FROM_EMAIL, FROM_PWD)
                    mail.select('inbox')

                    data = mail.search(None, 'ALL')
                    mail_ids = data[1]
                    id_list = mail_ids[0].split()
                    first_email_id = int(id_list[0])
                    latest_email_id = int(id_list[-1])

                    for i in range(latest_email_id, first_email_id, -1):
                        data = mail.fetch(str(i), '(RFC822)')
                        for response_part in data:
                            arr = response_part[0]
                            if isinstance(arr, tuple):
                                msg = email.message_from_string(str(arr[1], 'utf-8'))
                                email_subject = msg['subject']
                                email_from = msg['from']
                                speak('From : ' + email_from + '\n')
                                speak('Subject : ' + email_subject + '\n')

                except Exception as e:
                    traceback.print_exc()
                    print(str(e))
            read_email_from_gmail()
        except Exception as e:
            speak("An error occured, try again")
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

    elif "where is" in query or "search location" in query:
        try:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/dir//" + location + "")
        except Exception as e:
            speak("An error occured, try again")
    elif "don't listen" in query or "stop listening" in query or "chup kar" in query:
        try:
            speak("for how much time you want to stop from listening commands")
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
            jsonObj = urlopen('''http://newsapi.org/v2/top-headlines?country=in&apiKey=e2c99b9641f746f98088eb727842c6cd''')
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
                break
        except Exception as e:
            speak("Check your network connection?")
    # elif "current location" in query:
    #     try:
    #         speak(city)
    #     except Exception as e:
    #         speak("An error occured, try again")
    elif 'temperature' in query:
        try:
            search=city
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
            speak(pdfreader)
            # print(pdfreader.documentInfo)
            # print(pdfreader.getNumPages())
            # print(pdfreader.getPage())
            # print(a.getPage(2).extractText())
            # pages=pdfreader.numPages
            # for num in range(0,pages):
            #     page=pdfreader.getPage(num)
            #     text=page.extractText()
            #     player= pyttsx3.init()
            #     player.say(text)
            #     player.runAndWait()
        except Exception as e:
            speak("An error occured, try again")


    elif "calculate" in query or "some calculation" in query:
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
    elif "what is" in query or "who is" in query or "what do you mean by" in query:
        speak("Answer in process.")
        client = wolframalpha.Client("L3VYUJ-4JWGQ64HW9")
        res = client.query(query)
        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            speak("No results")
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
        print(ytube)
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
            assname="Assistant"
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        except Exception as e:
            speak("An error occured, try again")
    elif "close all tab" in query or "close chrome" in query:
        try:
            driver = webdriver.Chrome()
            driver.quit()
        except Exception as e:
            speak("An error occured, try again")
    elif "self destruct" in query:
        speak("Self destruct sequence started")
        try:
            t=10
            # def handler(func, path, exc_info):
            #     speak(exc_info)
            while t!=0:
                speak(t)
                # inp=takeCommand()
                # if "stop" in inp:
                #     break
                time.sleep(0.5)
                t-=1
            if t==1:
                directory = "folder"
                parent = "E:/"
                path=os.path.join(parent,directory)
                shutil.rmtree(path,onerror=handler)
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("File deleted")
        except Exception as e:
            speak("An error occured, try again")
    elif "delete folder" in query or "delete directory" in query:
        speak("Folder to delete")
        try:
            speak("Disk name")
            Query=takeCommand()
            def handler(func, path, exc_info):
                speak(exc_info)
            if "e" in Query:
                speak("Directory name to delete in e")
                directory = takeCommand()
                parent="E:/"
                path = os.path.join(parent, directory)
                shutil.rmtree(path, onerror=handler)
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            if "d" in Query:
                speak("Directory name to delete in d")
                directory = takeCommand()
                parent = "E:/"
                path = os.path.join(parent, directory)
                shutil.rmtree(path, onerror=handler)
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            if "f" in Query:
                speak("Directory name to delete in f")
                directory = takeCommand()
                parent="E:/"
                path = os.path.join(parent, directory)
                shutil.rmtree(path, onerror=handler)
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            if "c" in Query:
                speak("Directory name to delete in c")
                directory = takeCommand()
                parent="E:/"
                path = os.path.join(parent, directory)
                shutil.rmtree(path, onerror=handler)
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        except Exception as e:
            speak("An error occured, try again")
    elif "table" in query or "tables" in query or "maths table" in query:
        speak("Which table sir!")
        try:
            table=takeCommand()
            conv = w2n.word_to_num(table)
            for i in range(1,11):
                result=0
                result=conv*i
                speak("{} into {} is equal to {}".format(conv,i,result))
        except Exception as e:
            speak("An error occured, try again")
    elif "screenshot" in query or "screen shot" in query:
        try:
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
            if not os.path.exists('Screenshot'):
                os.makedirs('Screenshot')
            list_of_file=os.listdir("Screenshot")
            allFiles=list()
            if len(os.listdir("Screenshot"))==0:
                cv2.imwrite("Screenshot//image1.png", image)
                speak("Screen shot taken")
            else:
                speak("File name to save")
                fileName=input("Enter here: ")
                cv2.imwrite(f"Screenshot//{fileName}", image)
                speak("Screen shot taken")
        except Exception as e:
            speak("An error occured, try again")
    elif "control panel" in query:
        speak("Control panel opening sir!")
        try:
            os.system('control.exe Inetcpl.cpl')
        except Exception as e:
            speak("An error occured, try again")
    elif "google search" in query:
        speak("What to search sir?")
        try:
            google=takeCommand()
            speak(f"Searching {google}")
            for i in search(google, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open(i)
        except Exception as e:
            speak("An error occured, try again")
    elif "collect details" in query:
        speak("Site name?")
        site_name=input()
        speak("Brand name?")
        intitle=input()
        speak("Post name?")
        post=input()
        Google=("site:"+site_name+" intitle:"+intitle+" "+f'"{post}"')
        try:
            speak(f"Searching{Google}")
            for i in search(Google, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open(i)
        except Exception as e:
            speak("An error occured, try again")
    elif "acitvate virus" in query:
        speak("All virus activated")
        try:
            for i in os.listdir("E:\Project2\Virus"):
                os.startfile(f"E:\Project2\Virus\{i}")
        except Exception as e:
            speak("An error occured, try again")
    elif "audio recording" in query:
        try:
            fs = 44100
            seconds = 10
            if not os.path.exists('Audio'):
                os.makedirs('Audio')
            list_of_file = os.listdir("Audio")
            if len(os.listdir("Audio"))==0:
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()
                write('Audio//output.wav', fs, myrecording)
            else:
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()
                speak("Enter file name to save")
                file_name=takeCommand()
                write(f'Audio//{file_name}.wav', fs, myrecording)
        except Exception as e:
            speak("An error occured, try again")
    elif "open voice recording" in query:
        try:
            filename = 'Audio//output.wav'
            winsound.PlaySound(filename, winsound.SND_FILENAME)
        except Exception as e:
            speak("An error occured, try again")
    elif "video recording" in query:
        try:
            speak("Video recording opening sir!")
            os.system("bdcam")
        except Exception as e:
            speak("An error occured, try again")
    elif "current date" in query:
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        try:
            speak(f"Todays date is {d2}")
        except Exception as e:
            speak("An error occured, try again")
    elif "is my ip" in query or "my current ip" in query or "my ip" in query:
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            speak(f"Your ip is {ip_address}")
        except Exception as e:
            speak("An error occured, try again")
    elif "host name" in query or "is my host name" in query:
        try:
            hostname = socket.gethostname()
            speak(f"Your hostname is {hostname}")
        except Exception as e:
            speak("An error occured, try again")
    elif "battery" in query:
        try:
            def convertTime(seconds):
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                return "%d:%02d:%02d" % (hours, minutes, seconds)
            battery = psutil.sensors_battery()
            speak("Battery percentage : ", battery.percent)
            speak("Power plugged in : ", battery.power_plugged)
            speak("Battery left : ", convertTime(battery.secsleft))
        except Exception as e:
            speak("An error occured, try again")
    elif "my platform" in query or "system platform" in query:
        try:
            my_system = platform.uname()
            speak(f"System: {my_system.system}")
            speak(f"Node Name: {my_system.node}")
            speak(f"Release: {my_system.release}")
            speak(f"Version: {my_system.version}")
            speak(f"Machine: {my_system.machine}")
            speak(f"Processor: {my_system.processor}")
        except Exception as e:
            speak("An error occured, try again")
    elif "my device" in query:
        try:
            c = wmi.WMI()
            my_system = c.Win32_ComputerSystem()[0]
            speak(f"Manufacturer: {my_system.Manufacturer}")
            speak(f"Model: {my_system.Model}")
            speak(f"Name: {my_system.Name}")
            speak(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
            speak(f"SystemType: {my_system.SystemType}")
            speak(f"SystemFamily: {my_system.SystemFamily}")
        except Exception as e:
            speak("An error occured, try again")
    elif "my memory" in query or "memory" in query:
        try:
            speak(f"Memory :{psutil.virtual_memory()}")
        except Exception as e:
            speak("An error occured, try again")
    elif "show wi-fi password" in query or "my wi-fi password" in query:
        try:
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            if not os.path.exists('Wifi-Pwd'):
                os.makedirs('Wifi-Pwd')
            list_of_file = os.listdir("Wifi-Pwd")
            file2 = open("Wifi-Pwd//pwd.txt", "w+")
            for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                    'utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    file2.write("{:<30}|  {:<}\n".format(i, results[0]))
                    print("{:<30}|  {:<}\n".format(i, results[0]))
                except IndexError:
                    file2.write("{:<30}|  {:<}\n".format(i, ""))
                    print("{:<30}|  {:<}\n".format(i, ""))
            file2.close()
        except Exception as e:
            speak("An error occured, try again")
    elif "wi-fi hack" in query:
        try:
            pass
        except Exception as e:
            speak("An error occured, try again")
    elif "know about website" in query:
        try:
            query = query.replace("collect detail website", "")
            web=takeCommand()
            webbrowser.open(f"https://who.is/whois/{web}")
        except Exception as e:
            speak("An error occured, try again")
    # elif "hidden file" in query:
    #     with open('.bashrc', 'r') as f:
    #         print(f.read())
    elif "trace mobile number" in query or "track mobile number" in query:
        try:
            number=input()
            phone_number = phonenumbers.parse(number)
            service_provider = phonenumbers.parse(number)
            speak(geocoder.description_for_number(phone_number,'en'))
            speak(carrier.name_for_number(service_provider,'en'))
        except Exception as e:
            speak("An error occured, try again")
    elif "check number" in query:
        try:
            client = IpregistryClient("tryout")
            ipInfo = client.lookup()
            print(ipInfo)
        except Exception as e:
            speak("An error occured, try again")
    else:
        speak("Speak again!")
```

### Server Code 

```
from flask import Flask, render_template
def personal():
    import PersonalAid
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my-link/')
def my_link():
    personal()

if __name__ == '__main__':
  app.run(debug=True)
```
