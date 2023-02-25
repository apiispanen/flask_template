import requests
import os
API_KEY = os.getenv('API_KEY')

if API_KEY is not None: 
    print('The API key is found')
else:
    from creds import API_KEY
    print('The API_KEY environment variable is not set.')

import subprocess
import sys
import string
# import ssl

import openai
import json
from user_info import google_it, json_pull, json_update

def ai_response(prompt, networking = None, previous_conversation=None, API_KEY = API_KEY):
    openai.api_key = API_KEY
    temperature = 0.5
    model_engine = "text-davinci-002"
    
    if networking:
        update_strings = ["update",'edit', 'modify']
        reminder_strings = ["remind", 'who']
        first_word = prompt.split()[0].lower().translate(str.maketrans("", "", string.punctuation)).splitlines()[0]

        # print("first word: ",first_word)

        if first_word in update_strings or first_word in reminder_strings:
            temperature = 0
            inquire_prompt = "Based on the below prompt, what is this person's name?\n\n'"+prompt+"'"
            name = ai_response(inquire_prompt, networking=False).replace('\n','')
            print("NAME: "+name)
            name  = name.translate(str.maketrans("", "", string.punctuation))

            if first_word in update_strings:
                print("*** UPDATING USER ***")
                prompt = """Pretend you are building a JSON database called "People" that is in the following rough format (comments in "[]"):\n\n {"People": {"[PERSONS NAME]": {"School": "[SCHOOL]","Location": "[LOCATION]","Interests":"[INTEREST]", "Fun Facts":"[FUN FACTS]", "[OTHER RELEVANT FIELD NAME]":"[OTHER DATA]" }}}  \n\nBased on this design, what fields and keys would you make out of the following dialog:""" + prompt+"\n\nAnswer in JSON only, and with facts you are certain about."
                # print("UPDATE PROMPT: ",prompt)

            if first_word in reminder_strings:
                print("*** RETRIEVING USER ***")
                # What can you tell me about 
                user_response = json_pull(name)
                print("DATABASE (json_pull) RESPONSE",user_response)
                cleaned_name = list(user_response.keys())[0]
                user_json = user_response[cleaned_name]

                keys =  ['School', 'Location', 'Company']
                try:
                    relevant_info = [user_json[key] for key in user_json.keys() if key in keys] 
                except:
                    relevant_info = []
                if len(relevant_info)>0:
                    print("relevant info: ", relevant_info)
                else:
                    relevant_info = None
                # their_results = google_it(cleaned_name, other_info=relevant_info)
                # print("GOOGLE RESULT: "+their_results)
                # prompt = "Based on their Linkedin header: "+str(their_results)+"\n and their json data:\n"+str(user_response)+'\n Can you briefly summarize the person?'

                prompt = "Pretend you're an assistant for me. Based on their json file data below, can you briefly summarize this person?\n"+str(user_response)+'\n '



    if previous_conversation:
        # prompt = f"This is the Python Dictionary of all our previous conversations, logged as 'Question by me : Answer by you. Please read this before I ask the question, at the bottom.': {previous_conversation} Based on the JSON from before, {prompt}"
        prompt = f"This is a Python Dictionary of all my previous prompts to you in chronological order, logged as a Python Dictionary (format is 'Prompt #':'Prompt'). These are only questions or words I have already inquiried with you (prompts). Please take all this into consideration after I ask the question below.\n {previous_conversation}. \n\nPrompt: {prompt}"




    # NOW RUN THE PROMPT:
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=temperature,
        frequency_penalty=1
    )

    message = completions.choices[0].text
    print("Prompt:", prompt)
    print("AI Response:", message)
    if networking and first_word in update_strings:
        print("to feed into json_update:\n",name, message)
        json_update(name, message)
        message = name+" has been updated."
        print("******** JSON UPDATED ********")



    return message

# prompt = 'update robert piispanen - he works at carlson fabrication solution, is a business owner and has a dog named stella. On the weekends, he likes to go swimming at the lake.'


# """I'm writing a script that will log relevant information about a person. Can you highlight the conversation below with the following format?
# - Person 
# - Occupation (if applicable)
# - Company (if applicable)
# - Interesting facts (if applicable)

# Conversation below:
# "I just met Sam Casey who is an engineer designing his own app with ChatGPT. He currently works with a company called Mercury who does NFT development, which is very interesting. he gave me his email, but I can't read it. I also found that we share the name college - both of us went to Babson. He'll be back in San Francisco in a few months, so maybe I can meet with him then."
# """
# prompt=""" something here """
# conversation = ai_response(prompt, previous_conversation=load_conversation())

# print(conversation)

# save_conversation(prompt, conversation)