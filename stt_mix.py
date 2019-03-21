from tkinter import *
from stt import *
import speech_recognition as sr
import pyaudio
root =Tk()
def text_eng():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text="..."
        r.energy_threshold = 4000
        try:
            while(text!='enter'):
                print(text)
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                otpt.pack()
                audio = r.listen(source) #Starts Listening
                text = r.recognize_google(audio) #Recognizes audio in English 
        except: #When there is no notable speech
            print("Sorry, couldn't hear you!")
def text_hin():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text="Speak now"
        ans=''
        r.energy_threshold = 4000
        try:
            while(text!='enter'):
                print(text)
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                otpt.pack()
                audio = r.listen(source) #Starts Listening
                text = r.recognize_google(audio,language='hi-IN') #Recognizes audio in Hindi
        except: #When there is no notable speech
            print("Sorry, couldn't hear you!") 
def to_hin():
    lang='hi-IN'
def to_eng():
    lang='en-US'


#Heading
Head=Label(root,text="Talk to type",bg="Black",fg="white")
Head.pack(fill=X,pady=10)

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack()

#button
button1=Button(topFrame,text="CLICK TO BEGIN",fg="red",command=text_eng)
button1.pack()

eng=Button(topFrame,text="ENGLISH",fg="Blue",command=text_eng)
eng.pack(side="left",padx=10,pady=10)

hin=Button(topFrame,text="HINDI",fg="Purple",command=text_hin)
hin.pack(side="left",padx=10,pady=10)

#checkbox

c1=Checkbutton(root,text="COPY")
c1.pack(padx=10,pady=10)

c2=Checkbutton(root,text="Convert into text file")
c2.pack(padx=10,pady=10)



#text-field
otpt=Text(root)
otpt.pack()
root.mainloop()
