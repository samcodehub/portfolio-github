# pip install pydub
import pydub

from pydub import AudioSegment
from pydub.playback import Play

audio = AudioSegment.from_file("sound.wav")

audio.export("output.mp3", format="mp3")