# Nami
This code is a Python script for creating a virtual voice assistant named Nami that performs google searches and wikipedia lookups. It uses several libraries such as SpeechRecognition, Pyttsx3, and Wikipedia to recognize and process voice input, and to provide audio output.

First, the program initializes the libraries and asks the user for their name. It listens to the user's response, recognizes it using Google's speech recognition API, and extracts the name from the input. If the user's response is not recognized, the program prompts the user to try again. After obtaining the name, the program greets the user and explains what it can do.

The program then enters a loop where it listens to the user's voice input, recognizes it using Google's speech recognition API, and processes it. If the user's input contains the word "google", the program performs a Google search for the term following the word "for". If the user's input contains the word "wikipedia", the program looks up the term following the word "for" on Wikipedia and returns a summary. If the user's input contains the phrase "go to sleep", the program terminates. If the user's input contains the phrase "on hold", the program enters a standby mode where it listens for the user to say "wake up" to resume processing user input. If the user's input is not recognized, the program prompts the user to try again.

In between processing user input, the program outputs audio to provide feedback to the user, using Pyttsx3 to convert text to speech.
