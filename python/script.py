import requests
from pprint import pprint

endpoint = "https://api.assemblyai.com/v2/transcript"

#* submit a file for transcription and print the response
json = {
  "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"
}

headers = {
    "authorization": "b62141f4d92b43f8a0f018ae6c8e018c",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)
pprint(response.json())

#* submit a file for transcription with punctuation and casing turned off
json = {
  "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3",
  "punctuate": False,
  "format_text": False
}

headers = {
    "authorization": "b62141f4d92b43f8a0f018ae6c8e018c",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

pprint(response.json())

#* request a single transcript and print the response
response = requests.get(endpoint + "wnrteyqrr-8ac7-482d-a875-7126257cf842", headers=headers)

pprint(response.json())

#* request all transcripts and print the response, which includes the 200 most recent
response = requests.get(endpoint + "?limit=200&status=completed", headers=headers)

pprint(response.json())

#* delete single transcript and print the response
response = requests.delete(endpoint + "/wmn5lg0no-c821-4469-86cf-aa5afe494270", headers=headers)

pprint(response.json())

#* reads a local file and returns data
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
