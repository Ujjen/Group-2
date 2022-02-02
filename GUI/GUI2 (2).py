from tkinter import *
#import numpy as np
from tkinter.filedialog import askopenfilename,asksaveasfilename
#import librosa
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from dtw import dtw
from scipy.io.wavfile import read
from time import sleep
import speech_recognition as se
import wave
import RPi.GPIO as GPIO
import math


LARGE_FONT = ("Verdana", 12)

class GUI(Canvas):
    def __init__(self,master):
        super().__init__(master, bg="white", width="800",height="600")
        t= Label(master, text = 'GUI2', font=('Arial, 25'))
        
        t.pack()

    def buildGui(self, master):
        super().__init__(master)
        # Change buttons to GPIO record and save
        #btn_open = Button(self, text = "Display", command=lambda: compareAndPlot())
        #btn_open.place(x=0, y=0)
        #btn_save = Button(self, text = "Record", command=lambda: save_file())
        #btn_save.place(x=50, y=0)
        #self.pack()

def distance():
    input_data = read(r"""insert path of speech2.wav""")
    password_data = read(r"""insert path of speech.wav""")
    audio2 = passwordata[1]
    audio = inputdata[1]
    distList = []
    for i in range(0, 1024):
        distList.append(math.dist((0,audio[i]), (0, audio2[i])))

    if ((sum(distList) // len(disList)) <= 2 and (sum(distList) // len(disList)) >= 0):
        return True
    else
        return False

        
def plot():
    fig = Figure(figsize = (5, 5), dpi = 100)
    
    password_data = read(r"""insert path of speech.wav""")#
    input_data = read(r"""insert path of speech2.wav""")
    audio1 = input_data[1]
    
    audio2 = password_data[1]
    
    plot1 = fig.add_subplot(111)
    
    plot2 = fig.add_subplot(111)#
    
    plot1.plot(audio1)
    
    plot2.plot(audio2)#

    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()
    distance()


    

button = 25
running = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

a = sr.Recognizer()
with sr.Microphone() as source:
    print("Record a password...")
    audio = a.listen(source)

    # new addition to save the recording
    with open('speech.wav', 'wb') as f:
        f.write(audio.get_wav_data())


    data=a.recognize_google(audio)
    print("password saved.")
    


while running:
    if (GPIO.input(button) == GPIO.HIGH):
        with sr.Microphone() as source:
            a = sr.Recognizer()
            print("Say something...")
            audio2 = a.listen(source)
            
            # new addition to save the recording
            with open('speech2.wav', 'wb') as f:
                f.write(audio.get_wav_data())
                
            data2=a.recognize_google(audio2)
            if(data2 == data):
                print("correct password!!")
                plot()
                if (distance() == True):
                    break
                else:
                    continue
            else:
                print("wrong password try again")
    else:
        print("Push the button to record audio...")
        sleep(5)
        if(GPIO.input(button) == GPIO.HIGH):
            running = True
        else:
            running = False



WIDTH = 800
HEIGHT = 600


window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("GUI2")

s = GUI(window)
s.buildGui(window)
window.mainloop()

