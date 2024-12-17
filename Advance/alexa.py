import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

# engine = wikipedia.summary(person, 1)
# print(info)
# talk(info)def take_command():
def take_command():
        command = ""
        try:
            with sr.Microphone() as source:
                print('Listening...') 
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')    
                    print(command)
        except:
            print("Sorry I couldn't hear anything.")
        return command

