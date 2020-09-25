# First install package for youtube; "pip install pytube3"

#importing the module 
from pytube import YouTube 

yt = YouTube("Copy YouTube Link Here")
print(yt.title)

stream = yt.streams.first()
stream.download("Select Download Path")