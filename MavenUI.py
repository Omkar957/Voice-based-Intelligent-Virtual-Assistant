import sys
from MavenGUI import Ui_MavenUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import requests
import bs4
import pyjokes
import wolframalpha
from googletrans import Translator
import PyPDF2
from gtts import gTTS
import pywhatkit

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 169)


def Speak(audio):
    print(" ")
    Assistant.say(audio)
    print(f": {audio}")
    print(" ")
    Assistant.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")

    Speak("I am Maven Sir. Please tell me how can i help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bhamareomkar5@gmail.com', 'jimjimdot@5')
    server.sendmail('bhamareomkar5@gmail.com', to, content)
    server.close()


def Temp():
    search = "temperature in Pune"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = bs4.BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    Speak(f"The temperature outside is {temperature} celcius")
    print(f"The temperature outside is {temperature} celcius")


def WolfRam(query):

    api_key = "9AGTJ9-8X446AQY8K"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    Answer = next(requested.results).text

    try:
        Answer = next(requested.results).text
        return Answer

    except:
        Speak("The Command is not answerable Sir")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExe()

    def WolfRam(self, query):
        try:

            api_key = "9AGTJ9-8X446AQY8K"

            requester = wolframalpha.Client(api_key)

            requested = requester.query(query)

            Answer = next(requested.results).text
            return Answer

        except:
            Speak("The Command is not answerable Sir")
            return None

    def Reader(self):
        Speak("Tell me the name of the book")

        name = self.takeCommand()

        if 'india' in name:

            os.startfile(
                'D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\Books\\Rocket.pdf')
            book = open(
                'D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\Books\\Rocket.pdf', 'rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak(f"From which page i have to start reading ?")
            # int(input("ENter the page number"))
            numPage = int(self.takeCommand())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In which language , I have to read ")
            lang = self.takeCommand()


    def Calculator(self, query):

        Term = str(query)

        Term = Term.replace("Maven", "")
        Term = Term.replace("Plus", "+")
        Term = Term.replace("Minus", "-")
        Term = Term.replace("Divide", "/")
        Term = Term.replace("By", "/")
        Term = Term.replace("Multiply", "*")
        Term = Term.replace("into", "*")

        Final = str(Term)

        try:

            result = WolfRam(Final)
            Speak(f"{result}")

        except:

            Speak("The Command is Not Available Sir")

    def Temp(self, query):

        Term = str(query)

        Term = Term.replace("Maven", "")
        Term = Term.replace("In", "")
        Term = Term.replace("What is the", "")
        Term = Term.replace("temperature", "")

        temp_query = str(Term)

        if 'outside' in temp_query:

            var1 = "Temperature in Pune"

            answer = WolfRam(var1)

            Speak(f"{var1} is {answer} .")

        else:

            var2 = "Temperature in " + temp_query

            ans = WolfRam(var2)

            Speak(f"{var2} is {ans}")


    def takeCommand(self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio, language='en-in')
                print(f"You said   : {query}")

            except Exception as Error:
                print("Say that again please")
                return "none"
            return query.lower()

    def TaskExe(self):

        wishMe()

        while True:

            self.query = self.takeCommand().lower()

            if 'hello' in self.query:
                Speak("Hello Sir, I am Maven .")
                Speak("Your Personal AI Assistant")
                Speak("How may I help you")

            elif 'how are you' in self.query:
                Speak("I am fine Sir")
                Speak("What about you")

            elif 'i am good' in self.query:
                Speak("Okay Sir")

            elif 'break' in self.query:
                Speak("Okay Sir, You can call me when you want")
                Speak("Adios Amigo")
                break

            elif 'wikipedia' in self.query:
                Speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                Speak("According to Wikipedia")
                print(results)
                Speak(results)

            elif 'youtube' in self.query:
                Speak("Ok Sir, This is what I found for your Search")
                self.query = self.query.replace("Maven", "")
                self.query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                Speak("Done sir")

            elif 'google search' in self.query:
                Speak("This is what I Found for your search")
                self.query = self.query.replace("Maven", "")
                self.query = self.query.replace("google search", "")
                pywhatkit.search(self.query)
                Speak("Done Sir")

            elif 'website' in self.query:
                Speak("Ok Sir, Launching....")
                self.query = self.query.replace("Maven", "")
                self.query = self.query.replace("website", "")
                web1 = self.query.replace("open", "")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched Sir")

            elif 'play music' in self.query:
                music_dir = 'D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\mymusic'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                Speak(f"Sir,the time is {strTime}")
                print(f"Sir,the time is {strTime}")

            elif 'email to mana' in self.query:
                try:
                    Speak("What should i say?")
                    content = self.takeCommand()
                    to = "mrunmayeee.borse@gmail.com"
                    sendEmail(to, content)
                    Speak('Email has been sent!')
                    print('Email has been sent!')
                except Exception as e:
                    print(e)
                    Speak("Sorry Sir it was not done")

            elif 'notepad' in self.query:

                Speak("Tell Me The Query.")
                Speak("I Am Ready To Write.")

                writes = self.takeCommand()

                time = datetime.datetime.now().strftime("%H:%M")

                filename = str(time).replace(":", ".")+"-note.txt"

                with open(filename, "w") as file:

                    file.write(writes)

                path_1 = "D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\" + \
                    str(filename)

                path_2 = "D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\Database\\Notepad\\" + \
                    str(filename)

                os.rename(path_1, path_2)

                os.startfile(path_2)

            elif 'alarm' in self.query:
                Speak("Enter the time !")
                time = input(": Enter the time :")

                while True:
                    time_At = datetime.datetime.now()
                    now = time_At.strftime("%H:%M:%S")

                    if now == time:
                        Speak("Time to wakeup up Sir!")
                        playsound('wake.mpeg')
                        Speak("Alarm CLosed")

                    elif now > time:
                        break

            elif 'joke' in self.query:
                Speak(pyjokes.get_joke())

            elif 'read book' in self.query:
                self.Reader()

            elif 'calculate' in self.query:
                self.Calculator(self.query)

                self.Result = self.WolfRam(self.query)
                Speak(self.Result)

            if 'temperature' in self.query:
                self.Temp(self.query)

            else:
                self.Result = self.WolfRam(self.query)
                Speak(self.Result)


startFunctions = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.maven_ui = Ui_MavenUI()
        self.maven_ui.setupUi(self)

        self.maven_ui.pushButton.clicked.connect(self.startFunc)
        self.maven_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.maven_ui.movies_lab2 = QtGui.QMovie(
            "D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\Iron_Template_1.gif")
        self.maven_ui.label_2.setMovie(self.maven_ui.movies_lab2)
        self.maven_ui.movies_lab2.start()

        self.maven_ui.movies_lab3 = QtGui.QMovie(
            "D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\__1.gif")
        self.maven_ui.label_3.setMovie(self.maven_ui.movies_lab3)
        self.maven_ui.movies_lab3.start()

        self.maven_ui.movies_lab4 = QtGui.QMovie(
            "D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\initial.gif")
        self.maven_ui.label_4.setMovie(self.maven_ui.movies_lab4)
        self.maven_ui.movies_lab4.start()

        self.maven_ui.movies_lab5 = QtGui.QMovie(
            "D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\Health_Template.gif")
        self.maven_ui.label_5.setMovie(self.maven_ui.movies_lab5)
        self.maven_ui.movies_lab5.start()

        self.maven_ui.movies_lab6 = QtGui.QMovie(
            "D:\\Dracarys\\Python\\Kratin\\GUIMAVEN\\B.G_Template_1.gif")
        self.maven_ui.label_6.setMovie(self.maven_ui.movies_lab6)
        self.maven_ui.movies_lab6.start()

        startFunctions.start()


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())
