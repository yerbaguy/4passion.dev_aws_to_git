from youtube_transcript_api import YouTubeTranscriptApi

outls = []

tx = YouTubeTranscriptApi.get_transcript('Z6nkEZyS9nA&t=186s', languages=['en'])

for i in tx:

    outtxt = (i['text'])
    outls.append(outtxt)

    print(outtxt)
