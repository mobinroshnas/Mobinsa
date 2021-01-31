import pyttsx3
import speech_recognition as sr
import webbrowser
import tkinter as Tkinter
import os

def alexa():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        talk("how can I help you, sir?")
        voice = r.listen(source)
        command = r.recognize_google(voice)
        command = command.lower()
        if 'search' in command:
            talk("ok sir")
            command = command.replace("search" , "")
            open = "www.google.com/search?q=" + command
            webbrowser.open(open)
        if 'hello' in command:
            talk("hello how can I help you")
        if 'translate' in command:
            talk("ok sir")
            open = "https://translate.google.com/"
            webbrowser.open(open)
        if "what's your name" in command:
            talk("I do not have a name but it is the name of my maker is mobeen")
        if 'go to team' in command:
            talk("ok sir")
            open = "https://github.com/DevBax"
            webbrowser.open(open)
        if 'email' in command:
            talk("ok sir")
            open = "http://mail.google.com/"
            webbrowser.open(open)
        if "what's up" in command:
            talk("ok sir")
            open = "https://web.whatsapp.com/"
            webbrowser.open(open)
        if "whatsapp" in command:
            talk("ok sir")
            open = "https://web.whatsapp.com/"
            webbrowser.open(open)
        if 'music folder' in command:
            talk("ok sir")
            path = "H:\آهنگ"
            path = os.path.realpath(path)
            os.startfile(path)
        print(command)
def talk(audio):
    talk = pyttsx3.init()
    voices = talk.getProperty('voices')
    talk.setProperty('voice' , voices[0].id)
    talk.say(audio)
    talk.runAndWait()
top = Tkinter.Tk()
greeting = Tkinter.Button(text="Speek", command=alexa, width=25,
    height=5,)
greeting.pack()
top.mainloop()

