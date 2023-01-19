#Made by Dayal Prathap
#Made at January 14th, 2023
#TECHSA - GPT 3 - Version==1.0 -

import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY
from credentials import username, bot_name
import time
import os


conversation = ""
user_name = "Sir"
botname = "Sara"


openai.api_key = API_KEY

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=1) 
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

print("Program running successfully")
time.sleep(3)
print("This product was programmed by Dayal Prathap")
time.sleep(1)
print("This product is lincensed under "+user_name)
time.sleep(1)
print("**NOTE** This program wont save conversation ,Hence it wont remeber past information once you exit")
time.sleep(1)
engine.say("Hello serah here please start with your prompt when terminal displays 'listening'")





while True:
    with mic as source:
        print("\nlistening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening.\n")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "

    conversation += prompt 

    response = openai.Completion.create(model='text-davinci-003', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    conversation += response_str + "\n"

  

    print(response_str)
    engine.say(response_str)
    engine.runAndWait()
        

    


    