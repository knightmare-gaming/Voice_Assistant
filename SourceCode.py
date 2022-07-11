from asyncio import subprocess
from subprocess import call
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import pynput
import ctypes

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening  !") 
  
    assiname = "Asus Vivobook 14"
    speak("I am your Assistant")
    speak(assiname)

def takecommand():

    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")                       # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  
        return "None"  
    return query

if __name__ == '__main__':

    wishMe()

    while True:
        query = takecommand().lower()
        if "what can you do" in query:
            speak('''I can do multiple things, i can help you fetch information 
            from the web,tickle your funny bone,play videos,music
            ,help you to get your favorite holiday destination or even turn this PC off
            only on your voice command! Hahhh, enough of me bragging about myself
            go ahead and try yourself some features! best of luck''')

        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikepedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:                 #youtube opening
            speak(" OKAY, opening Youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:                  #google opening
            speak(" OKAY, opening Google")
            webbrowser.open("google.com")
       
        elif "open Geeks for Geeks" in query:         #geeksforgeeks opening
            speak(" OKAY, opening Geeks for geeks")
            webbrowser.open("geeksforgeeks.com")

        elif "play music" in query:                   #play musics opening
                                                      # music_dir = "C:\Users\User\OneDrive\Desktop\Programs\TEMP DOWNLOAD\Songs
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "shutdown computer" in query:            #shutdown computer
            speak("shutting the computer")
            os.system("shutdown /s /t")

        elif "What is your name" in query:
            speak("My name is Asus Vivobook")
            
        elif "where is your home" in query:           #me
            speak(" i have a special place in your heart!!!")
            
        elif 'how are you' in query:                  #me
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:      #me
            speak("It's good to know that your fine")

        elif "who are you" in query:                  #me
            speak("I am your virtual assistant Asus.")

        #elif "Open my youtube playlist" in query:
            #speak("OKay,opening your youtube playlist")
            #webbrowser.open("https://www.youtube.com/feed/library")

        elif "play" in query:
            speak("Alright,playing your request on youtube")
            z=("https://www.youtube.com/results?search_query="+ query)
            webbrowser.open(z)
        elif "Tata Steel" in query:
            z=query
            speak(" Okay, initiating request")
            webbrowser.open("https://www.google.com/finance/quote/"+z+"NSE:")
        elif "where is" in query:                     #where is bangalore command
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/ place/" + location + "")

        elif 'search' in query:                         #search
            query = query.replace("search","")     
            webbrowser.open(query)
            
        elif 'joke' in query:                           #joke 
            speak(pyjokes.get_joke())

        '''elif 'lock' or 'lock this PC' in query:
            ctypes.windll.user32.LockWorkStation()
            speak("Okay, Locking this PC")'''
            
               
        '''elif "restart" in query:                        #restart
            speak("restarting Your computer!! please wait!")
            subprocess.call(["shutdown", "/r"])'''
             
        elif "hibernate" in query or "sleep" in query:  #hibernate
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "What is your name ?" in query:#andsfwLKUEGFWAUHWF
            speak("My friends call me")
            speak(assiname)
            print("My friends call me",assiname)

        elif ("what is your education qualification") in query: #me
            speak('''i have qualified to be a certified assistant for you, 
            You can call me asus''')

        elif ("scam 1992 on youtube") in query:
            speak("Okay, playing BGM scam 1992 on youtube")
            webbrowser.open("https://youtu.be/6ttsxzzrOdY")

        elif("call") in query:                                  #me
            speak("Not possible in laptop")

        elif 'exit' or 'bye' or 'close' in query:        #me
            speak(" Bye bye see you later! ")
            exit()

#def math():
    if "multiply" or "into" in query:
        speak("what is the first number ?")
