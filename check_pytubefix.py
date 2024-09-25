from pytubefix import YouTube

yt = YouTube('https://www.youtube.com/watch?v=TE66McLMMEw')

print(len(yt.streams))
subtitles = yt.captions

print(subtitles)
