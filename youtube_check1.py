import urllib.request
from lxml.html import fromstring
import requests
from bs4 import BeautifulSoup

web_url = "https://www.youtube.com/watch?v=Z6nkEZyS9nA&t=186s"

r = requests.get(web_url)

content = urllib.request.urlopen(web_url).read()
doc = fromstring(content)
print("lkjasdf",doc)

#
#soup = BeautifulSoup(r.content, 'html5lib')

##soup = BeautifulSoup(r.content, 'html5lib')

##print(soup)

##video_tags = soup.findAll('video')
##print("total", len(video_tags), "videos found")
