from tkinter import *
from random import *
from tkinter.filedialog import askopenfilename,asksaveasfilename


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
b1.place(x=100, y=400)

b2 = Button(window, text="button 2", bg = "pink", fg = "blue", font=("Helvetica", 12), justify = CENTER)
b2.place(x=600, y=400)

b3 = Button(window, text="Open", bg = "pink", fg = "blue", font=("Helvetica", 12), justify = CENTER)
b3.place(x=400, y=400)


window.mainloop()


