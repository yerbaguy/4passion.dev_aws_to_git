from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.bypass_age_gate()
caption = yt.captions['a.en']
print("caption", caption)
#print("yt", yt)
#print("youtube-tite", yt.title)
#print("youtube-captions", yt.captions)
#print("youtube-captions-xmlcaptions", i

#import pytube

#yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
#yt = pytube.YouTube('https://www.youtube.com/watch?v=pvDOnqGbghU')
print(yt.captions)
#caption = yt.captions.get_by_language_code('en')
#print(yt)
#print(caption.generate.srt_captions())

