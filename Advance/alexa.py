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

def run_alexa():
    command = take_command()
    print(command)


    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)


    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("There are multiple results for this person , can you be more specific?")
        except wikipedia.exceptions.HTTPTimeoutError:
            talk("Sorry, I couldn't retrieve information at the moment.")        
    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relation with wifi')

    elif 'joke' in command:
        joke = pyjokes.get_jokes()
        talk(joke)
    else:
        talk('Please say the command again.')

while True:
    run_alexa()                                           

    