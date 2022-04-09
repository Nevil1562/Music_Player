from cProfile import label
from tkinter import *

root = Tk()
root.geometry("600x450")
root.title("Music Player")
root.iconbitmap(r'img\\log1.ico')

text = Label(root, text="Let's Play Music to Rock")
text.pack()

pic = PhotoImage(file="img\\log.png")
root.mainloop()