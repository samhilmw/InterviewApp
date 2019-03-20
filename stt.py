import speech_recognition as sr
import pyaudio
lang='en-US'
def text_eng():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text="Speak now"
        r.energy_threshold = 4000
        try:
            while(text!='stop'):
                print(text)
                audio = r.listen(source) #Starts Listening
                text = r.recognize_google(audio,language=lang) #Recognizes audio in English 
        except: #When there is no notable speech
            print("Sorry, couldn't hear you!")
def text_hin():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text="Speak now"
        ans=''
        r.energy_threshold = 4000
        try:
            while(text!='stop'):
                print(text)
                audio = r.listen(source) #Starts Listening
                text = r.recognize_google(audio,language=lang) #Recognizes audio in Hindi
        except: #When there is no notable speech
            print("Sorry, couldn't hear you!") 
def to_hin():
    lang='hi-IN'
def to_eng():
    lang='en-US'
