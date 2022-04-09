from cProfile import label
from tkinter import *
from pygame import mixer

root = Tk()
root.geometry("600x450")
root.title("Music Player")
root.iconbitmap(r'img\\log1.ico')

text = Label(root, text="Let's Play Music to Rock").pack()

def play():
    print("Lets play music")

pic = PhotoImage(file="img\\play6.png", height=100, width=100)
Button = Button(root,image = pic, height=100, width=100, command=play).pack()

root.mainloop()