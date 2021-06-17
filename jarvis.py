import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir')
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')

    speak("I am Jarvis. Please tell me how may I help you?")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognising...')
            query = r.recognize_google(audio, language="en-in")
            print("User-said: ",query)

        except Exception as e:
            print("Say that again please...")
            speak("Say that again please...")
            return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@xyz.com",'your_password')
    server.sendmail('youremail@xyz.com',to,content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing task based on query

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to wikipedia ")
            speak(results)

        elif "meet my" in query:
            greet = query.split()
            tospeak = "Hi" + greet[-1] + "I am Jarvis. Nice to meet you."
            speak(tospeak)

        elif "the time" in query:
            strTime = "Sir, the time is" + str(datetime.datetime.now().hour) + "hours" + str(datetime.datetime.now().minute) + "minutes"
            speak(strTime)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            Music = "E:\\Music"
            songs = os.listdir(Music)
            print(songs)
            os.startfile(os.path.join(Music,songs[random.randint(0,len(songs))]))

        elif "play web series" in query:
            speak("Which webseries you want to watch?")
            webseriesname = takeCommand()
            if "friends" in webseriesname:
                Friends = "E:\\web series\\FRIENDS"
                episodes = os.listdir(Friends)
                speak("Which season and episode")
                data = takeCommand()
                os.startfile(os.path.join(Friends,episodes[int(data[-1])+1]))
            

        elif "open code" in query:
            codePath = "C:\\Users\\RASHMI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "send email to Rohit" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "youremail@xyz.com"
                sendEmail(to,content)
                speak("The email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Rohit! I am not able to sent this email")

        elif "exit" in query:
            exit()
           