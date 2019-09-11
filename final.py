from tkinter import *
import speech_recognition as sr
from tkinter import messagebox

window = Tk()
window.title("Event Registration app")
window.geometry('700x400')
lbl = Label(window, text="St.JOSEPH'S COLLEGE OF ENGINEERING", anchor=CENTER, relief=RAISED)
lbl.grid(column=175, row=175)

#Finding Names From File
def find_name(key):
    #print("function entered")
    with open('names.txt','r') as f:
        temp= True
        while temp :
            try:
                temp= f.readline()
                values= temp.split(' ')
                if values[0]== key:
                    messagebox.showinfo('Hello', values[1]+"You have been succesfully registered for the event")
                    break
            except:
                print("Error indide FindValue Function")


#Defining speech handler
def handler():
    r = sr.Recognizer()
    m= sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
    with m as source:
        print("Say your Register Number!")
        audio = r.listen(source, timeout= 5.0, phrase_time_limit= 5.0)

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
            find_name(text.replace(' ', '').upper())
            #return text.replace(' ', '').upper()
        except:
            print('Sorry could not recognize your voice')
            #return "ERROR"

btn = Button(window, text="Tap to register...", command=handler)
btn.grid(column=200, row=200)
window.mainloop()
