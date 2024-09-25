from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import sys


if len(sys.argv) != 2:
    print("add a videoId and output fil name after a script name")
    sys.exit(1)


vid_id = sys.argv[1]
output_file = sys.argv[2]
yt_client = build(
        "youtube","v3", developerKey="AIzaSyDUWweYDFXkKW7jk8tGW5OMfZ2tkDdFTx4"
        )

def get_comments(client, video_id, token=None):

    response = (client.commentThreads().list(

        part = "snippet",
        videId = video_id,
        textFormat = "plainText",
        maxResults = 100,
        pageToken = token
        ).execut()
        )
    return response
#except HttpError as e:
#      print(e.resp.status)
#      return None
#except Exception as e:
#      print(e)
#      return None

comments = []
next = None

while True:
    resp = get_comments(yt_client, video_id, next)

    if not resp:
        break

    comments += resp["items"]
    next = resp.get("nextPageToken")

    if not next:
        break

print(f"Total comments fetched: {len(comments)}")

