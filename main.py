import pyttsx3
import speech_recognition as sr
import webbrowser
import tkinter as Tkinter
import os
import sqlite3

db = sqlite3.connect('database.db')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   fname TEXT,);
""")
db.commit()
def alexa():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        cur.execute('''SELECT * FROM users''')
        user = cur.fetchone()
        if user == None:
            talk("whats your name?")
            voice = r.listen(source)
            command = r.recognize_google(voice)
            cur.execute('INSERT INTO users VALUES(?)', (command,))
            db.commit()
            talk("tank you")
        else:
            cur.execute('''SELECT fname FROM users''')
            user = cur.fetchone()
            talks = "Hello," + user[0] + "how can I help you?"
            talk(talks)
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
        if 'my name is' in command:
            command = command.replace("my name is" , "")
            cur.execute('''SELECT fname FROM users''')
            user = cur.fetchone()
            cur.execute('UPDATE users SET fname = ? WHERE fname = ?' , (command,user[0]))
            db.commit()
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
