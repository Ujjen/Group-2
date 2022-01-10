from tkinter import *
from random import *



######MAIN PROGRAM LOOP#######
WIDTH = 800
HEIGHT = 800
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("GUI demo")
window.config(bg='BLACK')

# Label
l = Label(window, text = "Voice Authentication System", bg = "black", bd = 100, fg = "white", justify = RIGHT, padx = 10, pady = 10, font=("Helvetica", 26))
l.pack()

# buttons
b1 = Button(window, text="button 1", bg = "pink", fg = "blue", font=("Helvetica", 12), justify = CENTER)
b1.pack(side=LEFT)

b2 = Button(window, text="button 2", bg = "pink", fg = "blue", font=("Helvetica", 12), justify = CENTER)
b2.pack(side=RIGHT)


window.mainloop()


