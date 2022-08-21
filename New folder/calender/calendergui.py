# pip install tkcalendar
from tkinter import *
from tkcalendar import *

root = Tk()
root.title()
root.geometry('400x300')
root.resizable(False,False)
root.config(bg='orange')

cal = Calendar(root,selectmode='day',year=2022,month=1)
cal.pack(pady=10)

# define func to get selected date
def get_info():
    x = cal.get_date()
    current_date['text'] = x
    
Button(root,text='Get Info', command=get_info, fg='green').pack(pady=5)
current_date= Label(root, text='', font=('Arial,18'),fg='black',bg='orange')
current_date.pack(pady=5)

root.mainloop()
