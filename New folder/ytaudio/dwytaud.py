from pytube import YouTube 
# pip install pafy 
import pafy
# url of video
url = "https://youtu.be/ipNhJgULdAs"
# instant created
video = pafy.new(url)
# print title
print(video.title)
# print rating
print(video.rating)
# print view count
print(video.viewcount)
# print author and video length
print(video.author, video.length)
# print duration, likes, dislikes, description
print(video.duration, video.likes, video.dislikes, video.description)
bestaudio = video.getbestaudio()
bestaudio.download()