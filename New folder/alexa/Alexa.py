# pip install pyttsx3   to speak out or text to speech 
# pip install SpeechRecognition for the robot to listen to our voice  
# pip install pywhatkit to advance control on browser 
# pip install wikipedia  to get data from wikipedia
# pip install pyjokes to get funny jokes 

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()   # voice reconizer ready to listen
engine = pyttsx3.init()
voices = engine.getProperty('voices')   # get all voices from pyttsx3 package
engine.setProperty('voice', voices[1].id)    # choose second voice that is female voice


def talk(text):
    engine.say('i am your alexa')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)  # play the song on youtube 
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')   # 12 hours time 
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)  # get summary from wikipedia
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())   # get some random joke from pyjokes
    else:
        talk('Please say the command again.')


while True:
    run_alexa()