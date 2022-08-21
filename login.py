from tkinter import *
import tkinter.messagebox

def validate():
    name= entry_1.get()
    email= entry_2.get()
    country = c.get()
    programming = var2.get()
    gender = var.get()
    if (name == "" or email =="" or country == "" or programming == 0 or gender == 0):
        tkinter.messagebox.showinfo('Invalid Message Alert',"Field cannot be empty")
        
    else:
        tkinter.messagebox.showinfo('Success Message', "Successfully Registered")
        
root = Tk()
root.geometry('500x500')
root.title('log in')

label_0 = Label(root, text = 'log in',width = 20, font=("bold",20))
label_0.place(x=90, y=53)

label_1 = Label(root, text = 'Full Name',width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text = "Email",width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text = "Gender",width=20,font=("bold",10))
label_3.place(x=70,y=230)

var = IntVar()
Radiobutton(root, text="Male",padx = 5,variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20,variable=var, value=2).place(x=290,y=230)

lable_4 = Label(root, text ="Country",width=20,font=("bold",10))
lable_4.place(x=70,y=280)

list1 = ['USA','GERMANY','BELGUIM','FRANCE','TURKEY','GREECE','OTHER..']
c=StringVar()

droplist=OptionMenu(root, c,*list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240,y=280)

lable_4 = Label(root, text="Programming",width=20,font=("bold",10))
lable_4.place(x=85,y=330)
var1 = IntVar()


Checkbutton(root,text="java", variable=var1).place(x=235,y=330)
var2 =IntVar()
Checkbutton(root, text="Python", variable=var2).place(x=290,y=330)

Button(root,text="Submit", width=20,bg='blue',fg='white',command = validate).place(x=180,y=380)

root.mainloop()
