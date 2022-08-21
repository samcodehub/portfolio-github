# pip install moviepy
import moviepy.editor

# replace the parameter with the location of the video file
video = moviepy.editor.VideoFileClip("video_name.mp4")

audio_data = video.audio

# replace the parameter with the location of the video file along with filename
audio_data.write_audiofile("audio_name.mp3")