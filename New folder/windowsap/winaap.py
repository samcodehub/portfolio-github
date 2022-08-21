# pip install winapps
from tkinter import *
import winapps

# function to attach output 
def app():
    for item in winapps.search_installed(e.get()):
        name.set(item.name)
        version.set(item.version)
        Install_date.set(item.install_date)
        publisher.set(item.publisher)
        uninstall_string.set(item.uninstall_string)

# an object of tkinter 
master = Tk()
# set background color
master.configure(bg='old lace')

# variable classes in tkinter 
name = StringVar()
version = StringVar()
Install_date = StringVar()    
publisher = StringVar()
uninstall_string = StringVar()

# creating label for each information and grid method to place them  
Label(master, text="Enter App Name : ", font="arial 10 bold", bg="old lace").grid(row=0, sticky=W)

Label(master, text="Name :" ,bg="old lace").grid(row=2, sticky=W)
Label(master, text="Version :",bg="old lace").grid(row=3, sticky=W)
Label(master, text="Install Date :",bg="old lace").grid(row=4, sticky=W)
Label(master, text="Publisher :" ,bg="old lace").grid(row=5, sticky=W)
Label(master, text="Uninstall String :" ,bg="old lace").grid(row=6, sticky=W)

# creating label for class variable name using widget Entry
Label(master, text="", textvariable=name, bg="coral").grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=version, bg="aqua").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=Install_date, bg="bisque").grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=publisher, bg="yellow").grid(row=5, column=1, sticky=W)  
Label(master, text="", textvariable=uninstall_string, bg="teal").grid(row=6, column=1, sticky=W)

e = Entry(master, width=30)
e.grid(row=0, column=1)  

# creating a button using the widget
b = Button(master, text="Show", command=app, bg="seagreen")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)  

mainloop()
        