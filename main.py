print("************************************ RUNNING MAIN FILE ************************************")

import os
# from stt import speech_to_text
from prompt import *
from tts import tts, tts_string
from flask import Flask, request, render_template, jsonify
from flask import session
from db import get_people
audioContent = ''

print('enter getJSONReuslt', flush=True)

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def index():
    return render_template('voice.html')


@app.route('/about')
def about():
    # with open("conversations.json", "r") as f:
    #     data = json.load(f)
    data = get_people()
    it = iter(data['People']).__next__

    return render_template('about.html', data=data, it=it)

@app.route("/save_audio", methods=['POST'])
def save_audio():

    # process the audio data here
    
    # mark the function as called
    session['audio_saved'] = True
    
    # read the audio data from the request body
    prompt = request.json['words']
    
    # prompt = ' '.join([word['value'] for word in words if word])
    if len(prompt.split(' ')) > 1:
        print("YOUR PROMPT:", prompt.split(' '),  len(prompt))
        response = ai_response(prompt, networking=True).replace('\n','')
    else:
        response = "How can I help you?"
    audioContent = tts_string(response)
    # do something with the audio data here

    return jsonify({"audioContent": audioContent, "airesponse":response})


# if __name__ == "__main__":
app.secret_key = 'mysecretkey'
# app.config['TEMPLATES_AUTO_RELOAD'] = True


API_KEY = os.getenv('API_KEY')

if API_KEY is not None:
    # FOR RUNNING ON RAILWAY
    print("Running on Railway")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
else:
    # FOR RUNNING ON LOCAL
    print("Running on Railway")
    app.run(debug=False, port=int(os.getenv("PORT", default=5000)))



# ai_response("What are 5 words to describe a grouchy fucking pig?")