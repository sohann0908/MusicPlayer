#importing the necessary modules 
import pygame
import tkinter as tkr 
from tkinter.filedialog import askdirectory
import os

#setting application window
musicplayer = tkr.Tk()

#setting application title
musicplayer.title("Music Player")

#setting application geometry
musicplayer.geometry("450x350")

#asking for music directory
directory= askdirectory()

#setting music directory to current working directing
os.chdir(directory)

#crearing our songlist
#os.listdir() return the list containing name of entries in the directory given by path
songlist = os.listdir()

#creating the playlist
playlist = tkr.Listbox(musicplayer , font= "Cambria 14 bold" , bg="cyan2", selectmode=tkr.SINGLE)

#adding song to songlist to playlist
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos= pos+1

#intializing modules
pygame.init()
pygame.mixer.init()


#function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

#function for stop button
def ExitMusicPlayer():
    pygame.mixer.music.stop()

#function for pause button
def pause():
    pygame.mixer.music.pause()

#function for resume button
def resume():
    pygame.mixer.music.unpause()

#Creating Buttons

Button_play= tkr.Button(musicplayer,height=3,width=5,text="Play Music",font="Cambria 14 bold",command=play,bg="Lime green",fg="black")
Button_stop= tkr.Button(musicplayer,height=3,width=5,text="Stop Music",font="Cambria 14 bold",command=ExitMusicPlayer,bg="red",fg="black")
Button_pause= tkr.Button(musicplayer,height=3,width=5,text="Pause Music",font="Cambria 14 bold",command=pause,bg="yellow",fg="black")
Button_resume= tkr.Button(musicplayer,height=3,width=5,text="Resume Music",font="Cambria 14 bold",command=resume,bg="pink",fg="black")

Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")


var= tkr.StringVar()
songtitle= tkr.Label(musicplayer,font="Cambria 12 bold", textvariable=var)
songtitle.pack()
musicplayer.mainloop()










