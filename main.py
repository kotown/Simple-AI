import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio

engine = pyttsx3.init('sapi5') # specify which voice you will want the ai to have
voices = engine.getProperty('voices') # get the voice, one of two
engine.setProperty ('voice', voices[0].id)

def speak(audio):# function to make the ai speak
    engine.say(audio)
    engine.runAndWait()

def time():# function to tell the time 
    speak("Welcome back!")
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    speak(f"The current time is {str(time)}")
  
time() # call function to tell time
  
def wiki(): # to search on wikipedia
    speak("What would you like to know?")
    query = input("What would you like to know: \n")
    result = wikipedia.summary(query, sentences=2) #specify how many lines to read
    speak(" according to wikipedia: \n")
    print(result)
    speak(result)
    


def talk_to_me():
    # 1. Get input from user, convert to text and store 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening.. ")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    # 2. Save the info and make ai more believable 
    try:
        query = r.recognize_google(audio, language='en-in')
        speak("Got you, analysing")
        print("Analysing..")
        speak(f"You asked {query}")
        print(f"You asked {query}")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
        
    except Exception as e:
        print(e)
        speak(f"Say that again.")
        print(f"Say that again")

wiki() # call function to call online search
talk_to_me() # call function to briefly speak to ai