# pip install pyttsx3 wikipedia pyjokes

import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import urllib.parse
import os
import subprocess

def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported in Colab.")

        
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

def take_command():
    return input("You (type your command): ").lower()

def open_google_search(text):
    query = urllib.parse.quote(text)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def open_spotify_search(query):
    q = urllib.parse.quote(query)
    url = f"https://open.spotify.com/search/{q}"
    webbrowser.open(url)

def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if query.startswith("play"):
            song = query.replace("play", "").strip()
            if song:
                speak(f"Playing on Spotify: {song}")
                open_spotify_search(song)
            else:
                speak("Opening Spotify...")
                webbrowser.open("https://open.spotify.com/")

        elif query.startswith("spotify"):
            item = query.replace("spotify", "").strip()
            if item:
                speak(f"Searching Spotify for: {item}")
                open_spotify_search(item)
            else:
                speak("Opening Spotify...")
                webbrowser.open("https://open.spotify.com/")

        elif query.startswith("open spotify"):
            speak("Opening Spotify...")
            webbrowser.open("https://open.spotify.com/")

        elif "open https://open.spotify.com" in query or "spotify.com" in query or "spotify:" in query:
            speak("Opening Spotify link...")
            webbrowser.open(query.strip())

        ## ------- WIKIPEDIA ---------

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except:
                speak("Sorry, I couldn't find anything.")

        ## -------- YOUTUBE ----------
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com/")
        
        ## -------- CHATGPT ---------
        elif 'open chatgpt' in query:
            speak("Opening ChatGPT...")
            webbrowser.open("https://chat.openai.com/")
    

        ## ------- GOOGLE ---------
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")
        
        ## -------- DATE & TIME ---------

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
        
        elif 'date' in query or "today's date" in query or 'today date' in query:
            today = datetime.datetime.now().strftime("%A, %B, %d, %Y")
            speak(f"Today's date is {today}")

        ## ------- CALCULATOR ---------

        elif 'calculator' in query or 'open calculator' in query:
            speak("Opening Calculator...")
            try:
                subprocess.Popen(["calc.exe"])
            except Exception:
                try:
                    os.startfile("calc.exe")
                except Exception:
                    speak("Could not open Calculator.")
    
        ##  ------JOKE--------
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            speak("Searching Google for your query...")
            open_google_search(query)

run_assistant()
