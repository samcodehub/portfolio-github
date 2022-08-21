import speech_recognition as sr 
from pydub import AudioSegment
import os  

# conversion of video to audio 
AudioSegment.from_file('video.mp4').export("output.mp3", format="mp3")

# getting the audio from output.mp3
sound = AudioSegment.from_mp3("output.mp3")

# converting the audio to wav format
audio_file = "transcript.wav"
sound.export(audio_file, format="wav")

# setting up the recognizer
r = sr.Recognizer()

# recognizing text from source with help of google 
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
    
text = r.recognize_google(audio)
print(text)

with open("transcript.txt", "w") as f:
    f.write(text)

f.close()


