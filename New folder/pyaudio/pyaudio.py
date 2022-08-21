# pip install pydub

from pydub import AudioSegment
from pydub.playback import Play

audio1 = AudioSegment.from_file("audio1.wav")
audio2 = AudioSegment.from_file("audio2.wav")

combined_audio = AudioSegment.empty()

combined_audio = audio1 + audio2

combined_audio.export("output.mp3", format="mp3")