import requests
from pprint import pprint

endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3",
  "punctuate": False,
  "format_text": False
}

headers = {
    "authorization": "b62141f4d92b43f8a0f018ae6c8e018c",
    "content-type": "application/json"
}

# submit a file for transcription and print the response
response = requests.post(endpoint, json=json, headers=headers)
pprint(response.json())

# request a single transcript and print the response
response = requests.get(endpoint, headers=headers)
pprint(response.json())

# reads file and returns data
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
 
# uploads a local file and gets back an audio_url
headers2 = {'authorization': "b62141f4d92b43f8a0f018ae6c8e018c"}
response = requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers2,
                         data=read_file("../audio/convo.MP3"))
pprint(response.json())
