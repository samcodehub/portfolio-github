from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg='white')
root.title('TEXT-TO-SPEECH')

# heading
Label(root, text='Text-TO-SPEECH' , font='ariel 20 bold', bg='white').pack()
Label(root, text='SAMCODEHUB', font='ariel 15 bold', bg='white').pack(side= BOTTOM)      

# label 
Label(root, text='Enter Text', font='ariel 15 bold', bg='white').place(x=20, y=60)

# text variable
Msg= StringVar()

#ENTRY
entry_field = Entry(root, textvariable =Msg, width='50')
entry_field.place(x=20, y=100)

# define function
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text= Message)
    speech.save('v.mp3')
    playsound('v.mp3')
    
def Exit():
    root.destroy()
    
def Reset():
    Msg.set()
    
# button
Button(root, text = "PLAY", font= 'ariel 15 bold', command = Text_to_speech, width=4).place(x=25, y=140)   
Button(root, text= "EXIT", font= 'ariel 15 bold', command = Exit, bg='red').place(x=100, y=140)
Button(root, text= "RESET", font= 'ariel 15 bold', command = Reset).place(x=175, y=140) 

root.mainloop()
