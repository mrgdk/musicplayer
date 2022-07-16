from turtle import st
from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

#Commands
def select_song():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Please select a song")
    current_song = filename
    track= filename.split("/")[-1]
    
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title.config(fg="green", text=track)
        volume_label.config(fg="green", text="Volume : " + str(current_volume))
    except Exception as e:
            print(e)
            song_title.config(fg="red", text="Error playing track")
def volume_up():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="green", text="Volume : Max")
            return
        current_volume += 0.1
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title.config(fg="red", text="Track hasn't been selected yet")
def volume_down():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume : Muted")
            return
        current_volume -= 0.1
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title.config(fg="red", text="Track hasn't been selected yet")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title.config(fg="red", text="Track hasn't been selected yet")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title.config(fg="red", text="Track hasn't been selected yet")

#Main Screen
master = Tk()
master.title("Player")

#Labels
Label(master, text="Custom Music Player", font=("Calibri", 15), fg="red").grid(sticky="N", row=0, padx=120)
Label(master, text="Please select a music track you'd like to play", font=("Calibri", 12), fg="blue").grid(sticky="N", row=1)
Label(master, text="Volume", font=("Calibri",12), fg="blue").grid(sticky="N", row=4)
song_title = Label(master, font=("Calibri",12))
song_title.grid(sticky="N", row=3)
volume_label = Label(master, font=("Calibri", 12))
volume_label.grid(sticky="N", row=5)

#Buttons

Button(master, text="Select Song", font=("Calibri",12), command=select_song).grid(row=2,sticky="N")
Button(master, text="Pause",font=("Calibri",12), command=pause).grid(row=3,sticky="W")
Button(master, text="Resume",font=("Calibri",12), command=resume).grid(row=3,sticky="E")
Button(master, text="-",font=("Calibri",12), width=5, command=volume_down).grid(row=5,sticky="W")
Button(master, text="+",font=("Calibri",12), width=5, command= volume_up).grid(row=5,sticky="E")

master.mainloop()