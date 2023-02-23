# Networker
Get Past Small Talk - Your AI-Powered Networking Assistant

## Basic Summary
OpenAI has impressed the world with ChatGPT. Networker is an AI-powered tool that aims to help you overcome the barrier of small talk when networking. By helping you remember important details about people, it aims to facilitate more meaningful conversations and build deeper connections. It is the combination of OpenAI's text prompting algorithm da-vinci, combined with both Speechly and Google APIs. 

## Project Outcome
Once the Speech to text funcitonality is flushed out, we'll want to have the following features:
- Networking Assistant: Networker will take any data gathered from a conversation you've had and log it, including important details as well as important facts about the person/people you've interacted with, stored in a JSON format in a MongoDB database.
- Inquiry Assistant: Networker will gather information on you by asking rich, meaningful questions to get to know you, your connections, and help you to inquire more about life, acting as both an assistant and personal coach.

### Latest deployment is held on Railway and [can be found here](https://networker.up.railway.app/)


Py Scripts: 
- App
  - Central Application, made using TKinter for a GUI
- Prompt
  - OpenAI's API script, pulling the text data and submitting a response.
- STT (Speech to text)
  - Using Google Cloud's speech to text API, voice data is recognized as text for input in app.py. 
- TTS (Text to Speech)
  - Using Google Cloud's text to speech API, we can gather text and output speech here.
- conversation.js
  - Holds prior conversation data.

Autorization Scripts (not added to GH):
- creds.py - holds API Keys in a Python format
- google.json - holds google authorization payload

![Networker Demo](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1vw8y19iIVxi4UXhwbKLhA.png)

Setbacks
- Logic loops
- High payload to request memory and/or formatting
- Historical data not easily found.

Needs: 
- Better human recognition
- Memory virtually - via MongoDB
<br><br>
For more information, see our [Medium Post](https://medium.com/@andrewpiispanen/the-networker-project-cc8765c25f50).
<br><br>
Questions? Reach out to me:<br>
apiispanen@berkeley.edu<br>
Drew Piispanen