
from tkinter import *
# pip install textblob
from textblob import TextBlob

# Function to clear both text entry boxes
def clearAll() :
	# whole content of text entry area is deleted
	word1_field.delete(0, END)
	word2_field.delete(0, END)

# Function to get a corrected word
def correction() :
    # get a content from entry box
	input_word = word1_field.get()
    
    # create a TextBlob object
	blob_obj = TextBlob(input_word)
    
    # get a corrected word
	corrected_word = str(blob_obj.correct())

	# insert method inserting the value in the text entry box
	word2_field.insert(10, corrected_word)


# Driver code
if __name__ == "__main__" :
    # Create a GUI window
	root = Tk()
    
    # Set the background colour 
	root.configure(background = '#154c79')
    
    # Set the window size
	root.geometry("480x250")
    
    # set the name of tkinter GUI window
	root.title("Spell Corrector")
	
    # Create Spell Corrector Application: label
	headlabel = Label(root, text = 'Spell Corrector Application',font="arial 15 bold", bg = "#cce7e8")
	
	# Create a "Input Word": label
	label1 = Label(root, text = "Enter The Word :",
				 bg = '#cce7e8')
		
	# Create a "Corrected Word": label
	label2 = Label(root, text = "Corrected Word :",
				 bg = '#cce7e8')
	
	
	# grid method is used for placing the labels
	# padx keyword argument used to set padding along x-axis .
	headlabel.grid(row = 1, column = 1, pady=30)
	label1.grid(row = 2, column = 0)
	label2.grid(row = 4, column = 0, padx = 10)

		
	# Create a text entry box for typing the information.
	
	word1_field = Entry()
	word2_field = Entry()
		
	# padx keyword argument used to set padding along x-axis .
	# pady keyword argument used to set padding along y-axis .
	word1_field.grid(row = 2, column = 1, padx = 10, pady = 10)
	word2_field.grid(row = 4, column = 1, padx = 10, pady = 10)

		
	# Create a Correction Button and attached with correction function
	button1 = Button(root, text = "Get Correction", bg = "#3FCE3F",
								command = correction)
		
	button1.grid(row = 3, column = 1)
	
	# Create a Clear Button and attached with clearAll function
	button2 = Button(root, text = "Clear All", bg = "#F95858",
					 command = clearAll)
	
	button2.grid(row = 5, column = 1)
	
	# Start the GUI
	root.mainloop()

  

