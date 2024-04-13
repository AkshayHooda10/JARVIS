import pyttsx3
import speech_recognition as sr 
import datetime
import webbrowser
import wikipedia
import smtplib
import time
from subprocess import call 

start_time = time.time()
from clapdetect import MainClapExe
MainClapExe()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def v_mouse():
     call(['python', 'hand tracker.py'])
def download_settings():
     call(['python' , 'FileAutomator.py'])     
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def file_collector():
     call(['python','upload_button.py'])
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello Sir! Jarvis here to help!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e :
        print("Say that again please..")
        return "None"
    return query

def sendemail(to, content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('akshay21csu312@ncuindia.edu', 'Sasori@1029')
     server.sendmail('akshay21csu312@ncuindia.edu' , to, content)
     server.close()
if __name__ == "__main__":   
    
    wishme()
    while True:
        query = takeCommand().lower()
        sites = [
                ("Google", "https://www.google.com"),
                ("YouTube", "https://www.youtube.com"),
                ("Facebook", "https://www.facebook.com"),
                ("Amazon", "https://www.amazon.com"),
                ("Wikipedia", "https://www.wikipedia.org"),
                ("Twitter", "https://www.twitter.com"),
                ("Instagram", "https://www.instagram.com"),
                ("LinkedIn", "https://www.linkedin.com"),
                ("Reddit", "https://www.reddit.com"),
                ("Netflix", "https://www.netflix.com"),
                ("Pinterest", "https://www.pinterest.com")
            ]
        playlist = [
                ("Slow dancing in the dark","https://www.youtube.com/watch?v=K3Qzzggn--s"),
                ("Rockstar Made", "https://www.youtube.com/watch?v=EwdsnGfrd-k"),
            ]
        combined_list = sites + playlist

        for item in combined_list:
                if f"Open {item[0]}".lower() in query.lower() or f"Play {item[0]}".lower() in query.lower():
                    webbrowser.open(item[1])
                    if item in playlist:
                        speak(f"Playing {item[0]} for you..")
                    else:
                        speak(f"Opening {item[0]} for you..")
        if "Get Hyper".lower() in query.lower():
                speak("As an A I model i am not capable of doing that")
                musicPath = "C:\\Users\\hooda\\Downloads\\Rockstarmade"

                webbrowser.open("https://www.youtube.com/watch?v=EwdsnGfrd-k")
                speak("Hey look at me move i've finally understood Sarcasm.")
        if 'wikipedia' in query :
            speak('Searching Wikipedia..')
            query = query.replace("Wikipedia", " ")
            results = wikipedia.summary(query , sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
                elif 'email to akshay' in query:
            try:
                  speak("What should the email say?")
                  content = takeCommand()
                  to = "hoodaakshay@gmail.com"
                  sendemail(to, content)
                  speak("Email has been sent!")
            except Exception as e:
                   print(e)
                   speak("Sorry sir , I am not able to send the email at the moment!") 
        if "Thank You".lower() in query.lower():
                speak("You're welcome!ByeBye")
                exit()
        if "Download settings".lower() in query.lower():
             download_settings()
        if "recognize my hand movement".lower() in query.lower():
            speak("Got it sir. Initializing CATER")
            max_duration = input(speak("How long do you want to run it?"))
            v_mouse()
        if "upload file".lower() in query.lower():
             file_collector()
            
            
        
    
