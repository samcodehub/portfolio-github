import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

# creating the gui window
music_player = tk.Tk()

# set the title for window
music_player.title("Music Player")

# set the size of the window
music_player.geometry("350x350")

# ask the user to open the music folder
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

# showing all existing files in a list
play_list = tk.Listbox(music_player, font="arial 12 bold", bg='#FFCD38', selectmode=tk.SINGLE)

# a for loop to play all songs 
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
    
# initialize the pygame mixer
pygame.init()
pygame.mixer.init()

# a function to play the song
def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()
    
# a function to stop the song   
def stop():
    pygame.mixer.music.stop()

# a function to to pause the song    
def pause():
    pygame.mixer.music.pause()
    
# a function to unpause the song
def unpause():
    pygame.mixer.music.unpause()
    
# creating the labels
Button1 = tk.Button(music_player,  height=1, font="arial 12 bold", text="PLAY", command=play, bg="#541690", fg="white")
Button2 = tk.Button(music_player,  height=1, font="arial 12 bold", text="STOP", command=stop, bg="#FF4949", fg="white")
Button3 = tk.Button(music_player,  height=1, font="arial 12 bold", text="PAUSE", command=pause, bg="#FF8D29", fg="white")
Button4 = tk.Button(music_player,  height=1, font="arial 12 bold", text="UNPAUSE", command=unpause, bg="#D4D925", fg="white")

# StringVar() holds a string data where we can set text value and can retrieve it
var = tk.StringVar()

# create a label to display the title of the song 
song_title = tk.Label(music_player, font="arial 12 bold", textvariable=var)

# The pack() geometry manager organizes widgets in blocks 
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both")

# run the gui 
music_player.mainloop()