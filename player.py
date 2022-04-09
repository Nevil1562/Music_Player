from cProfile import label
from struct import pack
from tkinter import *
from matplotlib import scale
from pygame import mixer

root = Tk()
mixer.init()
root.geometry("600x450")
root.title("Music Player")
root.iconbitmap(r'img\\log1.ico')

text = Label(root, text="Let's Play Music to Rock").pack()

def play():
    print("Lets play music")
    mixer.music.load("songs\\Black.mp3")
    mixer.music.play()

play_pic = PhotoImage(file="img\\play6.png", height=100, width=100)
play_Btn = Button(root,image = play_pic, height=100, width=100, command=play).pack()

def stop():
    print("Stoping music")
    mixer.music.stop()
    
stop_pic = PhotoImage(file="img\\stop.png")
stop_btn = Button(root, image= stop_pic, height=100, width=100, command=stop).pack()

def set_volume(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)

volume = Scale(root,from_= 0,to= 100,orient= HORIZONTAL, command=set_volume)
volume.set(10)
volume.pack()

root.mainloop()