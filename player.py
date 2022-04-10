from cProfile import label
from fileinput import filename
from msilib.schema import File
from struct import pack
from tkinter import *
import tkinter
from tkinter import filedialog
import tkinter.messagebox
from matplotlib import scale
from pygame import mixer

root = Tk()
mixer.init()
root.geometry("600x450")
root.title("Music Player")
root.iconbitmap(r'img\\log1.ico')

menubar = Menu(root)
root.config(menu=menubar)

def browse_file():
    global filename
    filename =filedialog.askopenfilename()
    print(filename)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('About Player', 'This is a music player not your toy')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='About Us', command=about_us)

text = Label(root, text="Let's Play Music to Rock").pack()

def play():
    print("Lets play music")
    mixer.music.load(filename)
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