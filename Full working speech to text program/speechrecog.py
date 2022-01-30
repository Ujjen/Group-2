import speech_recognition as sr

a = sr.Recognizer()
with sr.Microphone() as source:
    print("say something...")
    audio = a.listen(source)
    data=a.recognize_google(audio)
    print(data)

