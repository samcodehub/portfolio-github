from tkinter import *

# import filedialog modules
from tkinter import filedialog

#function for opening the window  
def browseFiles():
    filename= filedialog.askopenfilename(initialdir = "/",title = "Select A File",filetype =(("Text Files","*.txt*"),("all files","*.*")))
    
    # change label content  
    label_file_explorer.configure(text="File Opend: "+filename)
    
# create the root window
window = Tk()

# set the window title  
window.title('File Explorer By SamCodeHub')

# set window size
window.geometry("450x250")

# set the window background color
window.config(background="wheat")

# create a file explorer label
label_file_explorer = Label(window,text="File Explorer Using Tkinter",font=('ariel',20,'bold'),width=26, height=2 , fg="maroon",)

button_explore = Button(window,text="Browse File",bg='hotpink',font=('ariel',10,'bold'),command= browseFiles)
button_exit = Button(window,text="Exit",bg='hotpink',font=('ariel',10,'bold'),command=exit)

# grid method to placing the widgets
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# let the window wait for any event 
window.mainloop()
