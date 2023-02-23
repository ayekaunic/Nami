# importing libraries
import speech_recognition as sr
import webbrowser
import wikipedia
import pyttsx3
import time

# initializing recognizer
ears = sr.Recognizer()

# initializing text-to-speech engine
nami = pyttsx3.init()

# asking for user's name
name = ''
print("hello. i am Nami. your virtual assistant. what is your name?")
nami.say("hello. i am Nami. your virtual assistant. what is your name?")
nami.runAndWait()
while True:
    print("listening...")
    try:
        with sr.Microphone() as source:
            ears.adjust_for_ambient_noise(source)
            audio = ears.listen(source, timeout = 81)
            name = ears.recognize_google(audio)
            name = name.split()[-1]     
            break           
    except sr.UnknownValueError:
        nami.say("sorry. i didn't get that. come again?")
        nami.runAndWait()
    except sr.WaitTimeoutError:
        nami.say("please tell me what your name is.")
        nami.runAndWait()

# greeting
greeting = f"nice to meet you {name}. how can i help you? i can perform google searches and wikipedia lookups."
print(greeting)
nami.say(greeting)
nami.runAndWait()

# ask user for input
while True:
    anything_else = True
    print("listening...")
    try:
        with sr.Microphone() as source:
            ears.adjust_for_ambient_noise(source)
            audio = ears.listen(source, timeout = 81)
            text = ears.recognize_google(audio)
            
            # perform action based on user input
    
        # if you want to perform a google search for 'xyz', say 'search google for xyz'
        if "google" in text.lower():
            search_term = text.split("for")[1]
            nami.say(f"searching google for: {search_term}")
            nami.runAndWait()
            url = "https://google.com/search?q=" + search_term
            webbrowser.open(url)
            nami.say("here you go")
            nami.runAndWait()
            time.sleep(1)
            
        # if you want to look up 'xyz' on wikipedia, say 'search wikipedia for xyz'
        elif "wikipedia" in text.lower():
            search_term = text.split("for")[1]
            nami.say(f"looking up {search_term} on wikipedia")
            nami.runAndWait()
            summary = wikipedia.summary(search_term, sentences = 2)
            nami.say("this is what i've learned: ")
            nami.runAndWait()
            time.sleep(1)
            nami.say(summary)
            nami.runAndWait()
            
        # if you want to turn off the voice assistant, say 'go to sleep nami'
        elif "go to sleep" in text.lower():
            print(f"alright {name}, have a good day!")
            nami.say(f"alright {name}, have a good day!")
            nami.runAndWait()
            break
        
        elif "on hold" in text.lower():
            print(f"okay {name}. i'll be here if you need me. just say, wake up, to wake me up!")
            nami.say(f"okay {name}. i'll be here if you need me. just say, wake up, to wake me up!")
            nami.runAndWait()
            while True:
                print("listening...")
                try:
                    with sr.Microphone() as source:
                        ears.adjust_for_ambient_noise(source)
                        audio = ears.listen(source, timeout = 81)
                        query = ears.recognize_google(audio)
                        if "wake up" in query.lower():
                            anything_else = False
                            nami.say("alright. i'm up. what do you want me to do?")
                            nami.runAndWait()
                            break
                except sr.UnknownValueError: continue
                except sr.WaitTimeoutError: continue
            
        else:
            nami.say("come again? what do you want me to do?")
            nami.runAndWait()
            anything_else = False
        
        time.sleep(1)
        if anything_else:
            nami.say("anything else?")
            nami.runAndWait()
            
    except sr.UnknownValueError:
        time.sleep(1)
        nami.say("did you say something? sorry. i did not understand. come again?")
        nami.runAndWait()
        continue
    except sr.RequestError:
        nami.say("sorry. having trouble accesing the internet. try again, later.")
        nami.runAndWait()
        continue