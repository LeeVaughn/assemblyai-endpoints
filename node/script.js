const axios = require("axios");
const fs = require("fs");

// create a new instance of axios with custom configurations to be used with most requests
const assembly = axios.create({
  baseURL: "https://api.assemblyai.com/v2",
  headers: {
    authorization: "b62141f4d92b43f8a0f018ae6c8e018c",
    "content-type": "application/json",
  },
});

// create a new instance of axios with custom configurations to be used with uploading local files
const assembly2 = axios.create({
  baseURL: "https://api.assemblyai.com/v2",
  headers: {
      authorization: "b62141f4d92b43f8a0f018ae6c8e018c",
      "content-type": "application/json",
      "transfer-encoding": "chunked",
  },
});

//* submit a file for transcription
assembly
  .post(`/transcript`, {
    audio_url: "https://cdn.assemblyai.com/upload/b7ca7b27-e5c4-46cd-b16f-11a78c5d249a"
  })
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

//* submit a file for transcription with punctuation and casing turned off
assembly
  .post(`/transcript`, {
    audio_url: "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3",
    punctuate: false,
    format_text: false
  })
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

//* submit a file for transcription with speaker labels
assembly
  .post(`/transcript`, {
    audio_url: "https://cdn.assemblyai.com/upload/c8b5b441-1832-4063-9997-c1e05d1e7a20",
    speaker_labels: true
  })
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

//* submit a file for transcription with auto chapters, sentiment, and disfluencies
assembly
  .post(`/transcript`, {
    audio_url: "https://github.com/LeeVaughn/assemblyai-endpoints/blob/master/audio/convo.MP3?raw=true",
    auto_chapters: true,
    sentiment_analysis: true,
    disfluencies: true
  })
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

//* request a single transcript
assembly
  .get(`/transcript/${"wxcbxobk7-9b07-46d7-b33e-a1dd8739ce32"}`)
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

//* request all transcripts, limited to the last 200
assembly
  .get(`/transcript?limit=200&status=completed`)
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

//* delete a single transcript
assembly
  .delete(`/transcript/${"w2hkc43aj-7cbb-4dbf-a360-183d1ecd4ca3"}`)
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));

//* read a local audio file then submit it to get back an audio_url
fs.readFile("../audio/convo.MP3", (err, data) => {
  if (err) return console.error(err);

  assembly2
      .post("/upload", data)
      .then((res) => console.log(res.data))
      .catch((err) => console.error(err));
});
