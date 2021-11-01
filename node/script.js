const axios = require("axios");

// create a new instance of axios with custom configurations
const assembly = axios.create({
  baseURL: "https://api.assemblyai.com/v2",
  headers: {
    authorization: "b62141f4d92b43f8a0f018ae6c8e018c",
    "content-type": "application/json",
  },
});

// submit a file for transcription
assembly
  .post(`/transcript`, {
    audio_url: "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"
  })
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));
  