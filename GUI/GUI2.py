from tkinter import *
import numpy as np
from tkinter.filedialog import askopenfilename,asksaveasfilename
import librosa
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from dtw import dtw
from scipy.io.wavfile import read
import pyaudio
import wave
# import RPi.GPIO as GPIO
#ssimport audiofilesforexpo

LARGE_FONT = ("Verdana", 12)

class GUI(Canvas):
    def __init__(self,master):
        super().__init__(master, bg="white", width="800",height="600")
        t= Label(master, text = 'GUI2', font=('Arial, 25'))
        
        t.pack()

    def buildGui(self, master):
        super().__init__(master)
        # Change buttons to GPIO record and save
        btn_open = Button(self, text = "Display", command=lambda: compareAndPlot())
        btn_open.place(x=0, y=0)
        btn_save = Button(self, text = "Record", command=lambda: save_file())
        btn_save.place(x=50, y=0)
        self.pack()

        
def compareAndPlot():
    fig = Figure(figsize = (5, 5), dpi = 100)

    input_data = read(r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\bird_caw1.wav")
    audio = input_data[1]
    plot1 = fig.add_subplot(111)
    plot1.plot(audio)


    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

    
def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.end, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    chunk = 1024
    sampled_format = pyaudio.paInt16
    chanels = 2

    smple_rt = 44400
    seconds = 4
    filename = r"C:\Users\r2d26\OneDrive\Desktop\Elenahelpstuff\bird_caw2.wav"

    pa = pyaudio.PyAudio()

    stream = pa.open(format=sample_format, channels=chanels,rate=smpl_rt, input=True,frames_per_buffer=chunk)
    print('Recording...')
    frames = []

    for i in range(0, int(smpl_rt / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    pa.terminate()
    print('Done !!! ')
    sf = wave.open(filename, 'wb')
    sf.setnchannels(chanels)
    sf.setsampwidth(pa.get_sample_size(sample_format))
    sf.setframerate(smpl_rt)
    sf.writeframes(b''.join(frames))
    sf.close()

WIDTH = 800
HEIGHT = 600


window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("GUI2")

s = GUI(window)
s.buildGui(window)
window.mainloop()

