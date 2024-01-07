import pyttsx3
import speech_recognition as sr 
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
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
                speak("SIKE YOU REALLY THOUGHT?")
        if 'wikipedia' in query :
            speak('Searching Wikipedia..')
            query = query.replace("Wikipedia", " ")
            results = wikipedia.summary(query , sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if "Thank You".lower() in query.lower():
                speak("Do tell me if help needed! ByeBye")
                exit()

    