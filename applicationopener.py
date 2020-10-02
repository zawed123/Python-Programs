#Hi codehouse Big Fan
#This app is built to easily open any application
#It's UI is Awesome and you will also like 
#Please import all the modules I have mentioned
import tkinter 
from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import PIL as ImageTk

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def opengoogle():
	speak("opening google.com")
	webbrowser.open("www.google.com")

def openyoutube():
	speak("opening youtube.com")
	webbrowser.open("www.youtube.com")

def openfacebook():
	speak("opening facebook.com")
	webbrowser.open("www.facebook.com")

def opendewan():
	speak("opening dewanpublicschoolmeerut website")
	webbrowser.open("https://dewanpublicschoolmeerut.org/")

def openppt():
	speak("opening Power Point PRESENTATION")
	os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk")

def openword():
	speak("opening Microsoft word")
	os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk")
def openwats():
	speak("opening whatsapp web")
	webbrowser.open("https://web.whatsapp.com/")

def time():
	now = datetime.datetime.now()
	print ("Current date and time : ")
	print (now.strftime("%Y-%m-%d %H:%M:%S"))

def opengmail():
	speak('opening gamil.com')
	webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

def quit1():
	root.destroy()

#google_img=PhotoImage(file=r"C:\Users\PCL\Desktop\JARVIS\image\google.png")

root= tkinter.Tk()
root.title("Abhra")
root.geometry("600x600")
root.configure(background="#00CCCD",bd=10)

time()

################ MY IMAGES ########################
#photo=PhotoImage(file=r"C:\Users\PCL\Desktop\JARVIS\image\google.png")

lbl1=Label(
	root,
	text=("Abhra's APPLICATION OPENER"),
	font=("Verdana",20,"bold"),
	bg="yellow",
	fg="red",
	width=50,
	relief= FLAT,
	bd=5
	)
lbl1.pack()

lbl2=Label(
	root,
	text=("One Place To Open Any Application"),
	font=("Verdana",20,"bold"),
	bg="#45CE30",
	fg="white",
	width=50,
	relief= GROOVE
	)
lbl2.pack()


google=Button(
	root,
	text=("GOOGLE.COM"),
	font=("Verdana",14,"bold"),
	#image=photo,
	command=opengoogle,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"
	)
google.pack(side=TOP)


youtube=Button(
	root,
	text=("YOUTUBE.COM"),
	font=("Verdana",14,"bold"),
	command=openyoutube,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"
	)
youtube.pack()

gamil=Button(
	root,
	text=("GMAIL.COM"),
	font=("Verdana",14,"bold"),
	command=opengmail,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"
	)
gamil.pack()

facebook=Button(
	root,
	text=("FACEBOOK.COM"),
	font=("Verdana",14,"bold"),
	command=openfacebook,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"
	)
facebook.pack()

dewan=Button(
	root,
	text=("DEWANs SCHOOL"),
	font=("Verdana",14,"bold"),
	command=opendewan,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"
	)
dewan.pack()

ppt=Button(
	root,
	text=("POWERPOINT PRESENTATION"),
	font=("Verdana",14,"bold"),
	command=openppt,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"
	)
ppt.pack()

word=Button(
	root,
	text=("MICROSOFT WORD"),
	font=("Verdana",14,"bold"),
	command=openword,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"
	)
word.pack()

wats=Button(
	root,
	text=("WHATSAPP WEB"),
	font=("Verdana",14,"bold"),
	command=openwats,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"

	)
wats.pack()

quit=Button(
	root,
	text=("WHATSAPP WEB"),
	font=("Verdana",14,"bold"),
	command=quit1,
	height=2,
	width=25,
	relief=GROOVE,
	bg="white",
	fg="black"

	)
quit.pack()







root.mainloop()
