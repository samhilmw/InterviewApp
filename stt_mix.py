from tkinter import *
from stt import *
import speech_recognition as sr
import pyaudio
root =Tk()

def text_eng():
    Head['text']='Start talking'
    Head.pack()
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        try:
            while(text!='enter'):
                print(text)
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                otpt.pack()
                audio = r.listen(source) 
                text = r.recognize_google(audio)  
        except: 
            Head['text']='Sorry, couldnt hear you! Try again'
            Head.pack()
    
def text_hin():
    Head['text']='Start talking'
    Head.pack()
    text=""
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text=""
        r.energy_threshold = 1000
        try:
            while(text!='रुक'):
                print(text)
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                otpt.pack()
                audio = r.listen(source) 
                text = r.recognize_google(audio,language='hi-IN')
        except: 
            Head['text']='Sorry, couldnt hear you! Try again'
            Head.pack()


def create_file():
    #name=str(E.get('1',END))
    name=E1.get()
    name=name+'.txt'
    stuff=otpt.get("1.0",END)
    f=open(name,'w+')
    f.write(stuff)
    f.close
    Head['text']='Created'
    Head.pack()
    
def copy():
    stuff=otpt.get("1.0",END)
    


#Heading
Head=Label(root,text="Talk to type",bg="Black",fg="white")
Head.pack(fill=X,pady=10)

topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack()

#button
#button1=Button(topFrame,text="CLICK TO BEGIN",fg="red",command=text_eng)
#button1.pack()

eng=Button(topFrame,text="ENGLISH",fg="Blue",command=text_eng)
eng.pack(side="left",padx=10,pady=10)

hin=Button(topFrame,text="HINDI",fg="Purple",command=text_hin)
hin.pack(side="left",padx=10,pady=10)

#checkbox

c1=Checkbutton(bottomFrame,text="COPY")
c1.pack(padx=10,pady=10)

#c2=Checkbutton(root,text="Convert into text file")
#c2.pack(padx=10,pady=10)

ctf=Button(bottomFrame,text="Convert to txt file",fg="red",command= lambda :  create_file())
ctf.pack(side="left",padx=10,pady=10)

E1 = Entry(bottomFrame, bd =5)
E1.pack(side="left",padx=10,pady=10)

#text-field
otpt=Text(root)
otpt.pack(side="bottom")


root.mainloop()



