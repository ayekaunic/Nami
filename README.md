# Nami
This code sets up a voice assistant called "Nami" that can perform various tasks based on voice commands. The tasks include performing Google searches, looking up information on Wikipedia, and translating English to Chinese.

The code starts by importing various libraries including speech_recognition, webbrowser, wikipedia, and pyttsx3. It then initializes the recognizer and text-to-speech engine. The user is then prompted to provide their name using speech input, which is recognized using the microphone and stored as a string variable.

After greeting the user, the code enters a loop where it continuously listens for user input using the microphone. The user can give various voice commands such as "search Google for [search term]", "search Wikipedia for [search term]", "say [text] in Chinese", and "go to sleep Nami".

When the user gives a command, the code performs the corresponding task. For example, if the user says "search Google for cats", the code will open a Google search for "cats" in a web browser. If the user says "search Wikipedia for dogs", the code will look up "dogs" on Wikipedia and read a summary of the article out loud. If the user says "say hello in Chinese", the code will translate "hello" to Chinese and read out the pronunciation.

If the user says "go to sleep Nami", the code will say goodbye and exit the loop, effectively turning off the voice assistant. If the user says "stay on hold", the code will enter a standby mode where it will continue to listen for voice commands but will not perform any actions until the user says "wake up".
