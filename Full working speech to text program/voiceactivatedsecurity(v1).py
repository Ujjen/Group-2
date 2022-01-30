import RPi.GPIO as GPIO
from time import sleep
import speech_recognition as sr

button = 25
running = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

a = sr.Recognizer()
with sr.Microphone() as source:
    print("Record a password...")
    audio = a.listen(source)
    data=a.recognize_google(audio)
    print("password saved.")


while running:
    if (GPIO.input(button) == GPIO.HIGH):
        with sr.Microphone() as source:
            a = sr.Recognizer()
            print("Say something...")
            audio2 = a.listen(source)
            data2=a.recognize_google(audio2)
            if(data2 == data):
                print("correct password!!")
                break
            else:
                print("wrong password try again")
    else:
        print("Push the button to record audio...")
        sleep(5)
        if(GPIO.input(button) == GPIO.HIGH):
            running = True
        else:
            running = False
        
        

