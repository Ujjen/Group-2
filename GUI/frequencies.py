from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from scipy.io.wavfile import read
from time import sleep
import speech_recognition as sr
import wave
import RPi.GPIO as GPIO
import math
import subprocess


def distance():
    input_data = read(r"/home/pi/speech.wav")
    password_data = read(r"/home/pi/speech2.wav")
    audio2 = password_data[1]
    audio = input_data[1]

    x=(sum(audio2) / len(audio2))
    y = (sum(audio) / len(audio2))

    print(x)
    print(y)

    print((x+y)/2)
    return True

        
def plot():


    fig = Figure(figsize = (5,5), dpi = 100)
    

    plt.figure(1, figsize = (30, 10))

    password_data = read(r"/home/pi/speech.wav")
    input_data = read(r"/home/pi/speech2.wav")

    fig = Figure(figsize = (7,7), dpi = 100)
    

    password_data = read(r"/home/pi/speech.wav")#
    input_data = read(r"/home/pi/speech2.wav")

    input1 = input_data[1]
    
    password3 = password_data[1]

    #plot1 = fig.add_subplot(111)
    plot1 = fig.add_subplot(150)
    plot1.plot(input1)

    #plot2 = fig.add_subplot(212)
    plot2 = fig.add_subplot(275)
    plot2.plot(password3)
    
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    distance()

def clear():
    exit()

button = 25
running = True



GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

a = sr.Recognizer()
avgL = [] 
for i in range(0,5):
    with sr.Microphone() as source:
        print("Record a password...")
        audio = a.listen(source)

        # new addition to save the recording
        with open(r"/home/pi/speech.wav", 'wb') as f:
            f.write(audio.get_wav_data())



        ###
            temp_data = read(r"/home/pi/speech.wav")
            temp = temp_data[1]
            avgL.append(sum(temp)/len(temp))
        ###

            data=a.recognize_google(audio)
            print("password saved.")

###
    avg = (sum(avgL) / len(avgL))
###

    
while running:
    if (GPIO.input(button) == GPIO.HIGH):
        with sr.Microphone() as source:
            b = sr.Recognizer()
            print("Say something...")
            audio2 = b.listen(source)
            
            # new addition to save the recording
            with open(r"/home/pi/speech2.wav", 'wb') as d:
                d.write(audio2.get_wav_data())
                
            data2=b.recognize_google(audio2)

            distance()
            if(data2 == data):
                print("correct password!!")
                subprocess.call(["xdg-open", '/home/pi/Desktop/images-gif'])
                print("password: {}".format(data))
                print("password attempt: {}".format(data2))
                plot()

                if (distance() == True):
                    # unlock the file or whatever
                    print("LETS FUCKING GOOOOOOOOOOOOO")
                    break
                else:
                    continue
            else:
                print("wrong password try again")
                
    elif(GPIO.input(button) == GPIO.LOW):
        print("Push the button to record audio...")
        sleep(5)
        if(GPIO.input(button) == GPIO.HIGH):
            running = True
        else:
            running = False


window = Tk()
window.geometry("500x500")
clear_button = Button(master = window, command = clear, height = 2, width = 10, text = "Clear")
clear_button.pack()
window.mainloop()


