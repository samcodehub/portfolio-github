
from tkinter import *

# create a gui window
window = Tk()
window.geometry('550x250')
window.title('Weight Converter By SamCodeHub')

# function to convert weight in kg to grams, pounds, ounces
def from_kg():
    # convert kg to gram  
    gram = float(e2_value.get())*1000  
    
    # convert kg to pounds
    pound = float(e2_value.get())*2.20462
    
    # convert kg to ounces
    ounce = float(e2_value.get())*35.274
    
    # enter the converted weight to the widgets
    t1.delete("1.0", END)
    t1.insert(END, gram)
    
    t2.delete("1.0", END)
    t2.insert(END, pound)
    
    t3.delete("1.0", END)
    t3.insert(END, ounce)
    
# create the widget label 
e1 = Label(window, text = "Enter the weight in kg:", font=('ariel',10,'bold'))
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = "Gram")
e4 = Label(window, text = "Pounds")
e5 = Label(window, text = "Ounce")

# create the text widgets
t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

# create the button widget
b1 = Button(window, text="Convert", command= from_kg)

# grid method to place widgets at respective positions 
e1.grid(row= 2, column=1, padx=20, pady= 50)
e2.grid(row= 2, column=2)
e3.grid(row= 5, column=1)
e4.grid(row= 5, column=2)
e5.grid(row= 5, column=3)
t1.grid(row=6, column=1)
t2.grid(row=6, column=2)
t3.grid(row=6, column=3, padx=15)
b1.grid(row=2, column= 3)

# start the gui
window.mainloop()