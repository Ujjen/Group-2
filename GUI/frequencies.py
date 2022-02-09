from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from scipy.io.wavfile import read
from time import sleep
import speech_recognition as sr
import wave
<<<<<<< HEAD
#import RPi.GPIO as GPIO
import math
import subprocess
import keyboard


def distance():
    input_data = read(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\speech.wav")
    password_data = read(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\speech2.wav")
=======
import RPi.GPIO as GPIO
import math
import subprocess

<<<<<<< HEAD
=======

def distance():
    input_data = read(r"/home/pi/speech.wav")
    password_data = read(r"/home/pi/speech2.wav")
>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66
    audio2 = password_data[1]
    audio = input_data[1]

    x=(sum(audio2) / len(audio2))
    y = (sum(audio) / len(audio2))

    print(x)
    print(y)

    print((x+y)/2)
    return True

        
def plot():
<<<<<<< HEAD
    fig = Figure(figsize = (5,5), dpi = 100)
    
    password_data = read(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\speech.wav")#
    input_data = read(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\speech2.wav")
=======


    fig = Figure(figsize = (5,5), dpi = 100)
    

    plt.figure(1, figsize = (30, 10))

    password_data = read(r"/home/pi/speech.wav")
    input_data = read(r"/home/pi/speech2.wav")

    fig = Figure(figsize = (7,7), dpi = 100)
    

    password_data = read(r"/home/pi/speech.wav")#
    input_data = read(r"/home/pi/speech2.wav")

>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66
    input1 = input_data[1]
    
    password3 = password_data[1]

    plot1 = fig.add_subplot(111)
<<<<<<< HEAD
    plot1.plot(input1)

    plot2 = fig.add_subplot(212)
    plot2.plot(password3)
    
    canvas = FigureCanvasTkAgg(fig, master = window)
=======
    #plot1 = fig.add_subplot(150)
    plot1.plot(input1)

    plot2 = fig.add_subplot(212)
    #plot2 = fig.add_subplot(275)
    plot2.plot(password3)
    
    canvas = FigureCanvasTkAgg(fig, master = "window")
>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    distance()

<<<<<<< HEAD
=======
>>>>>>> a94fdb34671b21e23d77c82bba71bee759a2e460
def clear():
    exit()
>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66

def distance():
    input_data = read(r"/home/pi/Desktop/wavfiles/speech2.wav")
    password_data = read(r"/home/pi/Desktop/wavfiles/speech.wav")
    audio2 = password_data[1]
    audio = input_data[1]

    avg_input = (sum(audio) / len(audio))
    
    # if statement to decide if the input is close enough to the avg password data
    print("avg "+str(avg))
    print("avg input "+str(avg_input))
    if (avg_input >= avg - 2) and (avg_input <= avg + 2):
        print(avg_input)
        print(avg)
        return True
    else:
        return False
    

        
def plot():
    fig = Figure(figsize = (10,10), dpi = 65)
    
    password_data = read(r"/home/pi/Desktop/wavfiles/speech.wav")#
    input_data = read(r"/home/pi/Desktop/wavfiles/speech2.wav")
    input1 = input_data[1]
    
    password = password_data[1]

    plot1 = fig.add_subplot(211)
    plot1.set_title("Password Data")
    plot1.plot(password)
    

    plot2 = fig.add_subplot(212)
    plot2.plot(input1)
    plot2.set_title("Input Data")
    
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    


button = 25
running = True
denied = False

<<<<<<< HEAD



#GPIO.setmode(GPIO.BCM)
#GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

a = sr.Recognizer()


with sr.Microphone() as source:
    print("Record a password...")
    audio = a.listen(source)

        # new addition to save the recording
    with open(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\speech.wav", 'wb') as f:
        f.write(audio.get_wav_data())

        temp = read(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\speech.wav")
        temp_list = temp[1]
        tempAvg = sum(temp) / len(temp)
        data=a.recognize_google(audio)
        print("password saved.")
        
while running:
    if (keyboard.is_pressed('ctrl')):
=======
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

window = Tk()
window.geometry("800x800")
clear_button = Button(master = window, text = "Clear", command = lambda : clear())
clear_button.pack()

a = sr.Recognizer()

avgL=[]

for i in range (0,3):
    with sr.Microphone() as source:
        print("Record a password...")
        audio = a.listen(source)

        # new addition to save the recording
        with open(r"/home/pi/Desktop/wavfiles/speech.wav", 'wb') as f:
            f.write(audio.get_wav_data())

            temp = read(r"/home/pi/Desktop/wavfiles/speech.wav")
            avgL.append(sum(temp[1]) / len(temp[1]))
            data=a.recognize_google(audio)
            print("password saved.")

print(avgL)
avg = (sum(avgL) / len(avgL))
print(avg)

while running:
    if (GPIO.input(button) == GPIO.HIGH):
>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66
        with sr.Microphone() as source:
            b = sr.Recognizer()
            print("Say something...")
            audio2 = b.listen(source)
            
            # new addition to save the recording
<<<<<<< HEAD
            with open(r"/home/pi/Desktop/wavfiles/speech2.wav", 'wb') as d:
                d.write(audio2.get_wav_data())
                
            data2=b.recognize_google(audio2)
            print("password: {}".format(data))
=======
<<<<<<< HEAD
            with open(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\speech2.wav", 'wb') as d:
                d.write(audio2.get_wav_data())
                
            data2=b.recognize_google(audio2)
=======
            with open(r"/home/pi/speech2.wav", 'wb') as d:
                d.write(audio2.get_wav_data())
                
            data2=b.recognize_google(audio2)
            print(data2)
>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66
>>>>>>> a94fdb34671b21e23d77c82bba71bee759a2e460

            if(data2 == data):
                #print("password: {}".format(data))
                print("password attempt: {}".format(data2))
                plot()

                if (distance() == True):
                    # unlock the file or whatever
                    print("ACCESS GRANTED")
                    subprocess.call(["xdg-open", '/home/pi'])
                    break
                else:
                    print("ACCESS DENIED")

            else:
                print("wrong password try again")


                
<<<<<<< HEAD
    elif(keyboard.is_pressed('ctrl')):
        print("Push the button to record audio...")
        sleep(5)
        if(keyboard.is_pressed('ctrl')):
=======
    elif(GPIO.input(button) == GPIO.LOW):
        print("Push the button to record audio...")
        
        while(GPIO.input(button) == GPIO.LOW):
            sleep(0.1)
        if(GPIO.input(button) == GPIO.HIGH):
<<<<<<< HEAD
            continue


=======
>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66
            running = True
        else:
            running = False
>>>>>>> a94fdb34671b21e23d77c82bba71bee759a2e460

<<<<<<< HEAD
window = Tk()
window.geometry("500x500")

window.mainloop()

        

<<<<<<< HEAD
=======
=======
window.mainloop()
>>>>>>> 8c6d08fe4661f2b8b9574537cb625b8a6461cd66
>>>>>>> a94fdb34671b21e23d77c82bba71bee759a2e460
