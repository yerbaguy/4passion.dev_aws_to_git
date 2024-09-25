import requests
from flask import Flask,jsonify
#from flask import Flask,request,jsonify
from youtube_transcript_api import YouTubeTranscriptApi as yta


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():
 return jsonify({"Hello":"World"})


@app.route('/check', methods=['GET'])
def get_check():
    #page = requests.get("https://www.youtube.com/watch?v=Z6nkEZyS9nA&t=186s")
    page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
    print("page",page)
    return page


@app.route('/get_split_word', methods=['GET'])
def get_split_word():
     #vid_id = "As3TT3xlddU&t=558s"
     vid_id = "xh2v5oC5Lx4"
     data = yta.get_transcript(vid_id)
     transcript = ''
     test = []
     test_val = []

     for value in data:
         for key, val in value.items():
             if key == "text":
                 #print(val)

                 #y = word_tokenize(val)
                 #print(val)

                 #if len(val) > 0:
                 #    val = val[0]
                 #    test.append(val)
                 #if len(val) >= 0:
                 #    print(val[1])
                 transcript += val

     outPut = transcript.splitlines()
     final_output = ''.join(outPut)



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
