from tkinter import *
from stt import *
root =Tk()


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

eng=Button(topFrame,text="ENGLISH",fg="Blue",command=to_eng)
eng.pack(side="left",padx=10,pady=10)

hin=Button(topFrame,text="HINDI",fg="Purple",command=to_hin)
hin.pack(side="left",padx=10,pady=10)

#checkbox

c1=Checkbutton(root,text="COPY")
c1.pack(padx=10,pady=10)

c2=Checkbutton(root,text="Convert into text file")
c2.pack(padx=10,pady=10)

'''texteditor
entry1=Entry(root)
entry1.pack()'''

#text-field
otpt=Text(root)
otpt.insert(INSERT,"from text-field")
otpt.pack()
root.mainloop()

