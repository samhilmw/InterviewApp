import speech_recognition as sr
import pyaudio
from tkinter import *
lang='en-US'
root =Tk()


def to_hin():
    lang='hi-IN'
def to_eng():
    lang='en-US'
def text_eng():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text="..."
        r.energy_threshold = 4000
        try:
            while(text!='stop'):
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                audio = r.listen(source) 
                text = r.recognize_google(audio)  
        except: 
            print("Sorry, couldn't hear you!")


#text-field
otpt=Text(root)

#Heading
head_txt="Talk to type"
Head=Label(root,text=head_txt,bg="Black",fg="white")
Head.pack(fill=X,pady=10)

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack()

#button
button1=Button(topFrame,text="CLICK TO BEGIN",fg="red",command=text_eng)
button1.pack()

eng=Button(topFrame,text="ENGLISH",fg="Blue",command=to_eng)
eng.pack(side="left",padx=10,pady=10)

hin=Button(topFrame,text="HINDI",fg="Purple",command=to_hin)
hin.pack(side="left",padx=10,pady=10)

#checkbox

c1=Checkbutton(root,text="COPY")
c1.pack(padx=10,pady=10)

c2=Checkbutton(root,text="Convert into text file")
c2.pack(padx=10,pady=10)

#pack
otpt.pack()
root.mainloop()
