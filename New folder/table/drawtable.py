from tkinter import *
class Table:
    def __init__(self,root):
        #code for creating the table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, fg='darkslategray',font=('Arial',14,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
                
lst = [(1,'jack','LA',19),
	(2,'brad','NY',18),
	(3,'lisa','WA',20),
	(4,'bernard','TX',21),
	(5,'david','FL',21)]

# find total number of the rows and columns
total_rows = len(lst)
total_columns = len((lst[0])) 

# creating the root window
root = Tk()
t = Table(root) 
root.mainloop()
