import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Adjusting the rate and volume for more natural voice
rate = engine.getProperty('rate')
engine.setProperty('rate', 176)  # You can experiment with different values
engine.setProperty('volume', 1)  # 0.0 to 1.0, 1.0 being the maximum volume

# Creating a function which will convert text to speech/voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

        # In case of an Exception 
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")

        except Exception as e:
            speak("Can you repeat that again...")
            return "none"
        query = query.lower()
        return query

# Let Sizcon wish you 
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if 0 < hour < 12:
        speak("Good Morning Buddy")
    elif 12 <= hour < 18:
        speak("Good Afternoon Buddy")
    else:
        speak("Good Evening Buddy")
    speak("How can I help you?")

def TaskExecution():
    wish()

    while True:
        # Creating Query to store user input 
        query = takeCommand().lower()  # Uncomment this line to capture user input

        # Logic building for tasks 
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open Instagram" in query:
            webbrowser.open("www.Instagram.com")
            
        elif " Search {query}" in query:
            webbrowser.open("www.google.com")

        elif "no thanks" in query:
            speak("see you Buddy let me know if you need any help")
            break

        speak("Buddy Do you have any more work to do")

# Anything written below this would be accessible in this file only
if __name__ == '__main__':
    
    while True:
        permission = takeCommand()
        if "wake up" in permission:
            TaskExecution()
        elif "bye" in permission:
            speak("Bye buddy, let me know if you need any help")
            sys.exit()

