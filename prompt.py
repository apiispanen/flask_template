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

from flask import session
import openai
import json
from user_info import google_it, json_pull, json_update
from user import person

def ai_response(prompt, networking = None, previous_conversation=None, API_KEY = API_KEY, temperature =.5):
    openai.api_key = API_KEY
    temperature = temperature
    model_engine = "text-davinci-003"

    if networking:
        update_strings = ["update",'edit', 'modify']
        reminder_strings = ["remind", 'who']
        ask_strings = ["what"]
        first_word = prompt.split()[0].lower().translate(str.maketrans("", "", string.punctuation)).splitlines()[0]

        inquire_prompt = "Based on the below prompt, what is this person's full name?\n\n'"+prompt+"'\n\nAnswer in as few characters as possible."
        human = person() 
        name = ai_response(inquire_prompt, networking=False, temperature=0).replace('\n',' ')
        human.name  = name.translate(str.maketrans("", "", string.punctuation))
        print(human.name)
        print("NAME VERIFIED: "+str(human.verify()))
        print("NAME: "+human.name)      
    
        if first_word in update_strings or first_word in reminder_strings or first_word in ask_strings:
            prompt = prompt.replace(name, human.name)
            temperature = 0
            if first_word in update_strings:
                print("*** UPDATING USER ***")
                prompt = """Pretend you are my assistant, building a JSON file called "People" that is in the following rough format (comments in "[]"):\n\n {"People": {"[PERSONS NAME]": {"School": "[SCHOOL]","Location": "[LOCATION]","Interests":"[INTEREST]", "Fun Facts":"[FUN FACTS]", "[OTHER RELEVANT FIELD NAME]":"[OTHER DATA]" }}}  \n\nBased on this design, what fields and keys would you make out of the following dialog:""" + prompt+"\n\nAnswer in JSON only, and with facts you are certain about. Do not respond with null fields, and only add new fields as necessary."
    

            if first_word in reminder_strings:
                print("*** RETRIEVING USER ***")
                # What can you tell me about 
                human_info = human.get_info()
                print(f"getting info for {human.name}:\n{human_info}")
                # print("DATABASE (json_pull) RESPONSE",human_info)
                
                linked_in = ''
                if "linkedin" in prompt or 'linked in' in prompt:
                    print("LINKEDIN FOUND")
                    linked_in = " and here is their LinkedIn info: \n"+ google_it(name)

                keys =  ['School', 'Location', 'Company']
                try:
                    relevant_info = [human_info[key] for key in human_info.keys() if key in keys] 
                except:
                    relevant_info = []
                if len(relevant_info)>0:
                    print("relevant info: ", relevant_info)
                else:
                    relevant_info = None

                prompt = f"Pretend you're an assistant for me. Based on their json file data below, can you briefly summarize this person?\n{human_info}\n{linked_in}"
                
            # if first_word in ask_strings:
            #     print("*** RETRIEVING USER ***")
            #     ai_response(f"What can you tell me about {human.name} based on the following?\n\n{human.get_info()}")

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
        print("to feed into json_update:\n",human.name, message)
        human.json = message
        human.update()
        message = str(human.name)+" has been updated."
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