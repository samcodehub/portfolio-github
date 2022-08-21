
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='hotpink', relief='raised')
canvas1.pack() 

label1 = tk.Label(root, text="IMAGE CONVERTER", bg='hotpink')
label1.config(font=('helvetica',20))
canvas1.create_window(150, 60, window=label1)

def getPNG():
        global im1
        import_file_path = filedialog.askopenfilename()
        im1 = Image.open(import_file_path)
        
browse_png = tk.Button(text="Selct PNG file", command=getPNG, bg="lime", fg='white', font=('helvetica',12, 'bold'))
canvas1.create_window(150, 100, window=browse_png)

def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)
    
saveasbutton = tk.Button(text="convert PNG to JPG", command=convert, bg= 'lime', fg='white', font= ('helvetica',12, 'bold'))
canvas1.create_window(150, 140, window=saveasbutton)
root.mainloop()