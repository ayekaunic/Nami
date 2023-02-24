# importing libraries
import speech_recognition as sr
import webbrowser
import wikipedia
import pyttsx3
import time
from translate import Translator
from pypinyin import lazy_pinyin
import re


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# initializing recognizer
ears = sr.Recognizer()

# initializing text-to-speech engine
nami = pyttsx3.init()

# asking for user's name
name = ''
print("\nhello. i am Nami. your virtual assistant. what is your name?")
nami.say("hello. i am Nami. your virtual assistant. what is your name?")
nami.runAndWait()
while True:
    print("\nlistening...")
    try:
        with sr.Microphone() as source:
            ears.adjust_for_ambient_noise(source)
            audio = ears.listen(source, timeout = 81)
            name = ears.recognize_google(audio)
            name = name.split()[-1]
            print(f"{CLEAR}")
            print(f"{CLEAR_AND_RETURN}")  
            break           
    except sr.UnknownValueError:
        print(f"{CLEAR}")
        print(f"{CLEAR_AND_RETURN}")
        nami.say("sorry. i didn't get that. come again?")
        nami.runAndWait()
    except sr.WaitTimeoutError:
        print(f"{CLEAR}")
        print(f"{CLEAR_AND_RETURN}")
        nami.say("please tell me what your name is.")
        nami.runAndWait()

# greeting
print(f"{CLEAR}")
print(f"{CLEAR_AND_RETURN}")
greeting = f"\nnice to meet you {name}. how can i help you? i can perform google searches and wikipedia lookups. i'm also pretty decent at chinese. although i have yet to nail down my pronounciations."
print(greeting)
nami.say(greeting)
nami.runAndWait()

# ask user for input
while True:
    anything_else = True
    print("\nlistening...")
    try:
        with sr.Microphone() as source:
            ears.adjust_for_ambient_noise(source)
            audio = ears.listen(source, timeout = 81)
            text = ears.recognize_google(audio)
            print(f"{CLEAR}")
            print(f"{CLEAR_AND_RETURN}")
            
        # perform action based on user input
    
        # if you want to perform a google search for 'xyz', say 'search google for [xyz]'
        if "google" in text.lower():
            search_term = text.split("for")[1]
            print(f"\nsearching google for: {search_term}")
            nami.say(f"searching google for: {search_term}")
            nami.runAndWait()
            url = "https://google.com/search?q=" + search_term
            webbrowser.open(url)
            nami.say("here you go")
            nami.runAndWait()
            time.sleep(1)
            
        # if you want to look up 'xyz' on wikipedia, say 'search wikipedia for [xyz]'
        elif "wikipedia" in text.lower():
            search_term = text.split("for")[1]
            print(f"\nlooking up {search_term} on wikipedia")
            nami.say(f"looking up {search_term} on wikipedia")
            nami.runAndWait()
            try:
                summary = wikipedia.summary(search_term, sentences = 2)
                print(f"{CLEAR}")
                print(f"{CLEAR_AND_RETURN}")
                print("\nthis is what i've learned: ")
                nami.say("this is what i've learned: ")
                nami.runAndWait()
                time.sleep(1)
                print(f"\n{summary}")
                nami.say(summary)
                nami.runAndWait()
            except:
                print(f"\nsorry {name}. i could not find anything on {search_term} on wikipedia. please try refining your query.")
                nami.say(f"sorry {name}. i could not find anything on {search_term} on wikipedia. please try refining your query.")
                nami.runAndWait()
                
        # to translate 'xyz' from english to chinese, say 'how do i say [xyz] in chinese'
        elif "chinese" in text.lower():
            to_translate = text
            translator = Translator(to_lang="zh")
            match = re.search(r'\bsay\s+(.*)\b(in chinese)?\b', to_translate, re.IGNORECASE)
            if match:
                to_translate = match.group(1)
                if match.group(2):
                    to_translate = ' '.join(to_translate.split()[:-2])
            try:
                chinese = translator.translate(to_translate)
                chinese = ' '.join(lazy_pinyin(chinese))
                print(f"{CLEAR}")
                print(f"{CLEAR_AND_RETURN}")
                print(f"\ntranslation: {chinese}")
                nami.say(f"that would be: {chinese}")
                nami.runAndWait()
            except:
                print(to_translate)
                print(chinese)
                anything_else =False
                print(f"\nsorry {name}. i didn't get that. come again?")
                nami.say(f"sorry {name}. i didn't get that. come again?")
                nami.runAndWait()
                
        # if you want to turn off the voice assistant, say 'go to sleep'
        elif "go to sleep" in text.lower():
            goodbye_message = f"alright {name}. Have a good day!"
            print(f"\n{goodbye_message}")
            nami.say(goodbye_message)
            nami.runAndWait()
            break
        
        # if you want it to be on stand by, say 'on hold'
        elif "on hold" in text.lower():
            print(f"\nokay {name}. i'll be here if you need me. just say, wake up, to wake me up!")
            nami.say(f"okay {name}. i'll be here if you need me. just say, wake up, to wake me up!")
            nami.runAndWait()
            while True:
                print("\nlistening...")
                try:
                    with sr.Microphone() as source:
                        ears.adjust_for_ambient_noise(source)
                        audio = ears.listen(source, timeout = 81)
                        query = ears.recognize_google(audio)
                        print(f"{CLEAR}")
                        print(f"{CLEAR_AND_RETURN}")
                        if "wake up" in query.lower():
                            anything_else = False
                            print("\nalright. i'm up. what do you want me to do?")
                            nami.say("alright. i'm up. what do you want me to do?")
                            nami.runAndWait()
                            break
                except sr.UnknownValueError: continue
                except sr.WaitTimeoutError: continue
            
        else:
            print(f"\nsorry {name}. i can only perform google searches and wikipedia lookups. try again.")
            nami.say(f"sorry {name}. i can only perform google searches and wikipedia lookups. try again.")
            nami.runAndWait()
            anything_else = False
        
        time.sleep(1)
        if anything_else:
            nami.say("anything else?")
            nami.runAndWait()
            
    except sr.UnknownValueError:
        time.sleep(1)
        print(f"{CLEAR}")
        print(f"{CLEAR_AND_RETURN}")
        nami.say(f"{name}? did you say something? sorry. i did not understand. come again?")
        nami.runAndWait()
        continue
    except sr.RequestError:
        print(f"{CLEAR}")
        print(f"{CLEAR_AND_RETURN}")
        nami.say(f"sorry {name}. i am having trouble accesing the internet. try again, later.")
        nami.runAndWait()
        continue