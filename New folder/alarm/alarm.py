from tkinter import *
from tkinter import messagebox
import datetime, time
from playsound import playsound    # pip install playsound

def button_hover(event):
    confirm["bg"] = "lightblue"
    
def button_hover_leave(event):
    confirm["bg"] = "SystemButtonFace"
    
def alarm(set_alarm):
    while True:
        current = datetime.datetime.now()
        date = current.strftime("%Y-%m-%d")
        time_atm = current.strftime("%H:%M:%S")
        if time_atm == set_alarm:
            print("wake up!!!")
            
        playsound("Happy_Home.mp3")
        break
    
def alarm_time():
    h = hour.get()
    m = minutes.get()
    answer = messagebox.showinfo("set_alarm",f"alarm will ringing at\n{h}:{m}")
    set_alarm = f"{h}:{m}:00"
    alarm(set_alarm)
    
 
    
if __name__ == "__main__":
    window = Tk()
    window.geometry("400x210")
    window.title = ("Alarm")
    
    choose_time = Label(text = "choose the alarm time")
    choose_time.place(x =20, y =20)
    
    hour = IntVar()
    Spinbox(width=4, from_=0, to=23, state="readonly", textvariable=hour
    ,wrap=True).place(x =200, y =20)
    
    minutes = IntVar()
    Spinbox(width=4, from_=0, to=59, state="readonly", textvariable=minutes, 
        wrap=True).place(x =240, y= 20)
    
    confirm = Button(text="set alarm", command=alarm_time, width=10, height=3)
    confirm.place(x =100, y =70)
    confirm.bind("<Enter>", button_hover)
    confirm.bind("<Leave>", button_hover_leave)
    
    exit = Button(text="Quit", width=10, command=window.destroy)
    exit.place(x=20, y=170)
    
    made_by = Label(text="made by SAMCODEHUB").place(x =260, y =170)
    window.mainloop()
