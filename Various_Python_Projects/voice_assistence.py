#Voice Assistence
#Google Text To speech;
from gtts import gTTS #google text to speech 
import speech_recognition as sr                       
import playsound                                           
from time import ctime
import os
import re
import uuid #universal unique id
import smtplib 
import webbrowser

#To make sure it listens
def listen():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking")
        audio = r.listen(source,phrase_time_limit=50)
    data = ""
    #Exception Handling
    try:
        data = r.recognize_google(audio,language="en-US")
        print("You said: "+data)
    except sr.UnknownValueError:  
        print("I can't hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
listen()

#To respond back with audio
def respond(String):
    print(String)
    tts = gTTS(text = String,lang = 'en-US')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#Start giving actions
#Virtual Assistant actions
def virtual_assistant(data):
        """give your actions"""

        if "how's you doing" in data:
            listening = True
            respond("Good and Doing well")

        if "time" in data:
            listening = True
            respond(ctime())

        if "open google" in data.casefold():
            listening = True
            url = "https://www.google.com"
            webbrowser.open(url)
            respond("Success")

        if "locate" in data:
            webbrowser.open("https://www.google.com/maps/search/"+data.replace("locate",""))
            result = "Located"
            respond("Located { }".format(data.replace("locate","")))

        if "email" in data:
            listening = True
            respond("Whom should i send email to?")
            to = listen().lower()
            edict = {"Hello" : "tanuriumakarthik@gmail.com"}
            toaddr = edict[to]
            respond("what is the Subject?")
            message = listen()
            respond("What should i tell that person?")
            message = listen()
            content = "Subject : {} \n \n {}".format(subject,message)

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com',587) #Host mail
            #Identify the server
            mail.ehlo()
            mail.starttls()
            #login
            mail.login("tanuriumakarthik@gmail.com","pzmq hhhq npxh zxuc")
            mail.send("tanuriumakarthik@gmail.com",toaddr,content)
            mail.close()
            respond("Email Sent")

        if "stop" in data:
            listening = False
            print("Listening Stopped")
            respond("Okay done take care....")

        try:
            return listening
        except UnboundLocalError:
            print("Timedout")
            
respond("Hey! Karthik I am fine")
listening = True
while listening == True:
    data = listen()
    listening = virtual_assistant(data) 

#Important packages to install from outside;
#pip install gtts
#pip install speechrecognition
#pip install playsound==1.2.2 #pip install pyaudio


        
