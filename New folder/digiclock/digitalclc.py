from tkinter import *
from tkinter.ttk import *

# importing strftime function to  retrieve system's time
from time import strftime

# creating tk window
root = Tk()
root.title('Digital Clock By SamCodeHub')

# function to display time on the label
def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

# Styling the label widget
lbl = Label(root, font = ('Arial', 40, 'bold'),
			background = 'maroon',
			foreground = 'white')

# Placing clock at the centre of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()
