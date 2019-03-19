import speech_recognition as sr
import pyaudio
r  = sr.Recognizer()
with sr.Microphone() as source:
    print("English or Hindi (e/h)")
    lang=input()
    text="Speak now"
    r.energy_threshold = 4000
    try:
        while(text!='stop'):
            print(text)
            audio = r.listen(source) #Starts Listening
            if(lang=='h'):
                text = r.recognize_google(audio,language='hi-IN') #Recognizes audio in Hindi
            else:
                text = r.recognize_google(audio) #Recognizes audio in English 
    except: #When there is no notable speech
        print("Sorry, couldn't hear you!")

