import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pyjokes
import pywhatkit
import os
import smtplib
from bs4 import BeautifulSoup
import requests
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

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
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tntprojectgp11', 'tnt@gp11')
    server.sendmail('tntprojectgp11', to, content)
    server.close()


if _name_ == "_main_":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'who is' in query:
            person = query.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'play' in query:
            song = query.replace('play', '')
            print(type(song))
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            topic = query.replace('search', '')
            speak('searching ' + topic)
            pywhatkit.search(topic)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()


        elif 'weather' in query:  

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
 
            def weather(city):
                city = city.replace(" ", "+")
                res = requests.get(
                    f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                print("Searching...\n")
                soup = BeautifulSoup(res.text, 'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                time = soup.select('#wob_dts')[0].getText().strip()
                info = soup.select('#wob_dc')[0].getText().strip()
                weather = soup.select('#wob_tm')[0].getText().strip()
                print(location)
                speak(location)
                print(time)
                speak(time)
                print(info)
                speak(info)
                print(weather+"°C")
                speak(weather+"degree celcius")
            
            place = query.replace('weather', '')
            city = place
            city = city+" weather"
            weather(city)
            print("Have a Nice Day:)")
        
        elif 'send email to' in query:
            t6 = query.replace('send email to', '')
            t5=t6.replace("anand","anandfcs")
            t4=t5.replace("kit","kiit.ac.in")
            t3=t4.replace("dot",".")
            t2=t3.replace("at","@")
            t1=t2.replace(" ","")
            print(t1)
            speak(t1)

            
            speak("What should I say?")
            content = takeCommand()
            if 'exit' in content:
                pass
            else:
                to = t1
                sendEmail(to, content)
                speak("Email has been sent!")
            

        elif 'send whatsapp to' in query:
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            contact = query.replace('send whatsapp to', '') 
            s1 = contact.replace("plus", "+")
            s2 = s1.replace(" ","")
            print(s2)
            speak(s2)

            speak("What should I say?")
            content = takeCommand()
            if 'exit' in content:
                pass
            else:
                pywhatkit.sendwhatmsg(s2,content,hour,minute+2)
