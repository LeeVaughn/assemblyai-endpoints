import requests
from config import auth_key
from pprint import pprint

endpoint = "https://api.assemblyai.com/v2/transcript"

# # #* submit a file for transcription and print the response
# json = {
#   "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"
# }

# headers = {
#     "authorization": "auth_key",
#     "content-type": "application/json"
# }

# response = requests.post(endpoint, json=json, headers=headers)
# pprint(response.json())

# #* submit a file for transcription with punctuation and casing turned off
# json = {
#   "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3",
#   "punctuate": False,
#   "format_text": False
# }

# headers = {
#     "authorization": "auth_key",
#     "content-type": "application/json"
# }

# response = requests.post(endpoint, json=json, headers=headers)

# pprint(response.json())

# #* submit a dual-channel file for transcription and print the response
json = {
  "audio_url": "https://cdn.assemblyai.com/upload/7c99e515-2fa7-4ff8-a476-52ea0cc09e8c",
  "dual_channel": True
}

headers = {
    "authorization": "auth_key",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)
pprint(response.json())

# #* request a single transcript and print the response
# headers = {
#     "authorization": "auth_key",
#     "content-type": "application/json"
# }

# response = requests.get(endpoint + "wnrteyqrr-8ac7-482d-a875-7126257cf842", headers=headers)

# pprint(response.json())

# #* request all transcripts and print the response, which includes the 200 most recent
# headers = {
#     "authorization": "auth_key",
#     "content-type": "application/json"
# }

# response = requests.get(endpoint + "?limit=200&status=completed", headers=headers)

# pprint(response.json())

# #* delete single transcript and print the response
# headers = {
#     "authorization": "auth_key",
#     "content-type": "application/json"
# }

# response = requests.delete(endpoint + "/wmn5lg0no-c821-4469-86cf-aa5afe494270", headers=headers)

# pprint(response.json())

# #* reads a local file and returns data
# def read_file(filename, chunk_size=5242880):
#     with open(filename, 'rb') as _file:
#         while True:
#             data = _file.read(chunk_size)
#             if not data:
#                 break
#             yield data
# # uploads a local file and gets back an audio_url
# headers = {'authorization': "auth_key"}
# response = requests.post('https://api.assemblyai.com/v2/upload',
#                          headers=headers,
#                          data=read_file("../audio/convo.MP3"))
# pprint(response.json())
