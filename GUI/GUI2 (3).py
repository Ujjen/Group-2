from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from scipy.io.wavfile import read
from time import sleep
import speech_recognition as sr
import wave
#import RPi.GPIO as GPIO
import keyboard
import math
#ssimport audiofilesforexpo



def distance():
    input_data = read(r"x")
    password_data = read(r"x")
    audio2 = password_data[1]
    audio = input_data[1]

    print(sum(audio2) / len(audio2))
    print(sum(audio) / len(audio))

    print((sum(audio2)+sum(audio))/2)
    return True
    
    

        
def plot():
    plt.figure(1, figsize = (30, 10))
    password_data = read(r"x")#
    input_data = read(r"x")
    input1 = input_data[1]
    
    password3 = password_data[1]

    plt.subplot(211)
    plt.plot(input1)

    plt.subplot(212)
    plt.plot(password3)
    plt.show()
    
    distance()


    

button = 25
running = True
avgL = []


#GPIO.setmode(GPIO.BCM)
#GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

a = sr.Recognizer()

for i in range(0,5):
    with sr.Microphone() as source:
        print("Record a password...")
        audio = a.listen(source)

        # new addition to save the recording
        with open(r"x", 'wb') as f:
            f.write(audio.get_wav_data())

        temp = read(r"x")
        temp_list = temp[1]
        tempAvg = sum(temp) / len(temp)
        avgL.append(tempAvg)

        data=a.recognize_google(audio)
        print("password saved.")
print(sum(avgL))
avg = sum(avgL) / len(avgL)
print(avg)
while running:
    if (GPIO.input(button) == HIGH):
        with sr.Microphone() as source:
            b = sr.Recognizer()
            print("Say something...")
            audio2 = b.listen(source)
            
            # new addition to save the recording
            with open(r"x", 'wb') as d:
                d.write(audio2.get_wav_data())
                
            data2=b.recognize_google(audio2)
            print("password: {}".format(data))
            print("password attempt: {}".format(data2))
            plot()
            distance()
            if(data2 == data):
                print("correct password!!")

                if (distance() == True):
                    # unlock the file or whatever
                    print("LETS FUCKING GOOOOOOOOOOOOO")
                    break
                else:
                    continue
            else:
                print("wrong password try again")
    if else(GPIO.input(button) == LOW):
        print("Push the button to record audio...")
        sleep(5)
        if(keyboard.is_pressed('q')):
            running = True
        else:
            running = False
        





