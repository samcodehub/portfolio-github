from tkinter import *

# function for clearing all contents of all entry boxes 
def clear_all():
    # whole content of entry boxes is deleted
    principle_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)
    
    # set focus on the principal_field entry box
    principle_field.focus_set()  

# function to find compound interest
def calculate_ci():
    # get a content from entry box  
    principle = int(principle_field.get())  
    rate = float(rate_field.get())
    time = int(time_field.get())
    # calculate compound interest
    CI = principle * (pow((1 + rate / 100), time))
    
    # insert method inserting the value in the text entry box
    compound_field.insert(10, CI)
# driver code  
if __name__ == "__main__":
    # create a gui window
    root = Tk()
    
    # set the background color of the window
    root.configure(background= 'tomato')
    
    # set the name of the window
    root.title("Interest Calculator By SamCodeHub")
    
    # set the size of the window
    root.geometry('400x250')
    
    # create a principle amount label
    label1 = Label(root, text = "Principle Amount($) : ", fg= 'white', bg= 'maroon' )
    
    # create a rate label
    label2 = Label(root, text = "Rate(%) : ", fg= 'white', bg= 'maroon')
    
    # create a time label
    label3 = Label(root, text = "Time(years) : ", fg= 'white', bg= 'maroon')
    
    # create a compound interest label
    label4 = Label(root, text = "Compound Interest : ", fg= 'white', bg= 'maroon')
    
# grid method is used to placing the widgets at a certain position
# padx keyword argument used to set the padding along x axis
# pady keyword argument used to set the padding along y axis
label1.grid(row=1, column=0, padx=10, pady=10)
label2.grid(row=2, column=0, padx=10, pady=10)
label3.grid(row=3, column=0, padx=10, pady=10)
label4.grid(row=4, column=0, padx=10, pady=10)

# Create a entry box for typing the information
principle_field = Entry(root)
rate_field = Entry(root)
time_field = Entry(root)
compound_field = Entry(root)

principle_field.grid(row=1, column=1, padx=10, pady=10)
rate_field.grid(row=2, column=1, padx=10, pady=10)
time_field.grid(row=3, column=1, padx=10, pady=10)
compound_field.grid(row=5, column=1, padx=10, pady=10)

# Create a submit button and attached to calculate_ci function
button1 = Button(root, text="Submit", bg="teal", fg= "white", command= calculate_ci)
# create a clear button to attached clear_all function
button2 = Button(root, text= "Clear", bg="darkred", fg= "white", command= clear_all)

button1.grid(row= 4, column= 1, pady=10)
button2.grid(row= 6, column= 1, pady=10)

# start the gui  
root.mainloop()


    