__version__ = '0.1.8'
import requests
import json 
from langchain.schema import (AIMessage, HumanMessage, SystemMessage)

url = "https://bettershot-w6mm.zeet-berri.zeet.app/openai_listener"

# def log(messages, completion, user_email, openai_api_key): 
#     payload = {
#     "messages": messages,
#     "completion": completion,
#     "openai_api_key": openai_api_key
#     }
#     headers = {
#         "Content-Type": "application/json",
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(payload))
#     print(response)
#     return {"response" : response}

def log(messages, completion, user_email, openai_api_key, query):
    raw_messages = []
    for message in messages: 
        if isinstance(message, SystemMessage):
            # messages': [{'role': 'user', 'content': "Hey! how's it going?"}]
            raw_message = {"role": "system", "content": message.content}
        elif isinstance(message, HumanMessage):
            raw_message = {"role": "system", "content": message.content}
        elif isinstance(message, AIMessage):
            raw_message = {"role": "ai", "content": message.content}
        else: 
            raw_message = message
        raw_messages.append(raw_message)
    if isinstance(completion, AIMessage):
        raw_completion = {"choices":[{"message": {"content": completion.content}}]}
    else: 
        raw_completion = completion
    payload = {
        "messages": raw_messages,
        "completion": raw_completion,
        "openai_api_key": openai_api_key, 
        "user_email": user_email, 
        "user_query": query
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response)
    return {"response" : response}