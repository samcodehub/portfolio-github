import tkinter as tk
from tkinter import ttk
from PIL import Image
from bs4 import BeautifulSoup
import requests, threading

# if user agent not work search on chrome my user agent otherwise update chrome
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def Weather(*args):
    global city
    city1 = city.get() + " weather"
    city1 = city1.replace(" ", "+")

    search_label['text'] = "Searching For "+city.get()
    

    res = requests.get(f'https://www.google.com/search?q={city1}&oq={city1}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    # print(soup.select('#wob_dts'))
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    tk.Label(root, text=location, font='Caveat 12 bold', bg="#2E2E2E", fg='#fff').place(x=130, y=250)
    tk.Label(root, text=info, font='ROBOTO 15 bold', bg="#2E2E2E", fg='#fff').place(x=130, y=220)
    tk.Label(root, text=f'{weather}°C', font='ROBOTO 35 bold', bg="#2E2E2E", fg='#fff').place(x=5, y=220)

    time = time.split(',')
    tk.Label(root, text=time[0], font='Caveat 20 bold', bg="#33FFDD", fg='#2E2E2E').place(x=330, y=210)
    tk.Label(root, text=time[1].upper(), font='ROBOTO 15 bold', bg="#33FFDD", fg='#2E2E2E').place(x=325, y=240)
    search_label['text'] = ""
    entry.delete('0', tk.END)


def call_function(*args):
    T = threading.Thread(target=Weather, daemon=True)
    T.start()


# making tkinter window
root = tk.Tk()
root.geometry("450x300")
root.title('Weather App SamCodeHub')
root.resizable(False, False)
# this is our app icon 
root.iconbitmap('cloudy.ico')

# set frames for show different content and color in window
frame1 = tk.Frame(root, bg='#fff', width=450, height=200)
frame1.place(x=0, y=0)

frame2 = tk.Frame(root, bg='#2E2E2E', width=300, height=100)
frame2.place(x=0, y=200)

frame3 = tk.Frame(root, bg='#33FFDD', width=150, height=100)
frame3.place(x=300, y=200)

# weather details
global city
city = tk.StringVar()

# make entry box take city name
tk.Label(root,  text="Enter the City Name", font=("Arial Rounded MT Bold", 12), bg="#fff").place(x=150, y=40)
entry = tk.Entry(root, textvariable=city,font=("Arial",13),bd=2,justify=tk.CENTER,relief=tk.GROOVE, width=18, bg='#D0FFBC')
entry.bind("<Return>",call_function)
entry.place(x=130, y=85)

tk.Button(root, text='Check', font=("Arial Rounded MT Bold", 10),bd=2,relief=tk.GROOVE, bg="#D0FFBC", command=call_function).place(x = 300, y=85)

search_label = tk.Label(root,  text="", font=("Sitka Small", 12), fg="#24292F",bg='#fff')
search_label.place(x=140, y=130)


root.mainloop()
