print("************************************ RUNNING MAIN FILE ************************************")

# import pyaudio
import wave
import os
# from stt import speech_to_text
from prompt import *
from tts import tts, tts_string
# import subprocess
# import sys
# import pydub
from flask import Flask, request, render_template, jsonify
# from sound import *
from flask import session
audioContent = ''

print('enter getJSONReuslt', flush=True)

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def index():
    return render_template('voice.html')


@app.route('/people')
def people():
    with open("conversations.json", "r") as f:
        data = json.load(f)
    it = iter(data['People']).__next__

    return render_template('people.html', data=data, it=it)

# @app.route('/startRecording')
# def startRecording(guiAUD=guiAUD):
#     guiAUD.startRecording()
#     return "On"

# @app.route('/stopRecording')
# def stopRecording(guiAUD=guiAUD):
#     guiAUD.stopRecording()
#     text_result = speech_to_text()
#     transcript = text_result.transcript
#     confidence = text_result.confidence 
#     response = ai_response(transcript)
#     tts(response)
#     return 'Off'


@app.route("/save_audio", methods=['POST'])
def save_audio():

    # process the audio data here
    print("Running save_audio() function")
    
    # mark the function as called
    session['audio_saved'] = True
    
    # read the audio data from the request body
    prompt = request.json['words']
    # prompt = ' '.join([word['value'] for word in words if word])
    print("YOUR PROMPT:", prompt)
    response = ai_response(prompt, networking=True)
    # print(response)

    
    audioContent = tts_string(response)
    # do something with the audio data here

    return jsonify({"audioContent": audioContent})




    # filename = 'temp/post_output.mp3'
    # with open(filename, "wb") as f:
    #     f.write(audio)
    # f.close()
    ### Check if file is present: 
    # if os.path.isfile(filename) and os.access(filename, os.W_OK):
    #     print(f"{filename} exists and is writable")
    # else:
    #     print(f"{filename} either does not exist or is not writable")


    # response = ai_response(transcript)
    # # response = ai_response(transcript, previous_conversation=load_conversation())

    # save_conversation(transcript)

    # print(response)

    # # ADD THE TEXT CONFIDENCE AND RESPONSE TO THE PROMPT
    # # self.add_response(transcript, response, confidence)
    # tts(response)



# if __name__ == "__main__":
app.secret_key = 'mysecretkey'
# app.config['TEMPLATES_AUTO_RELOAD'] = True

# FOR RUNNING ON RAILWAY
# app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# FOR RUNNING ON LOCAL
app.run(debug=False, port=int(os.getenv("PORT", default=5000)))

# ai_response("What are 5 words to describe a grouchy fucking pig?")