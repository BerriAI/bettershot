# bettershot 💡🚀

⚡️ A Python package for adding error monitoring to LLM Apps in a few minutes ⚡

>BetterShot by BerriAI let’s you add error (hallucinations/refusal to answer) monitoring to your LLM App in a few minutes. Like Bugsnag/Sentry for LLM apps!

## Getting Started 

Install bettershot by running this command.:

`pip install bettershot`

## Using bettershot

It's just 1 line of code: 

`log(messages=messages, completion=result, user_email="YOUR_EMAIL", query=query)`

<img width="1038" alt="Screen Shot 2023-06-13 at 10 08 36 AM" src="https://github.com/ClerkieAI/bettershot/assets/17561003/977ee3b6-3ed9-4d28-9aeb-35794dcb44b2">

### Dashboard 

All your logs are available @ 'https://better-test.vercel.app/' + YOUR_EMAIL

e.g. 
`log(messages=messages, completion=result, user_email="krrish@berri.ai", query=query)`

will have it's results logged @ 

`https://better-test.vercel.app/krrish@berri.ai`

### Implementation

Here are all the items you can log: 

| Parameter | Type | Required/Optional | Description |
| --------- | ---- | ----------------- | ----------- |
| `messages` | List | Required | The list of messages sent to the OpenAI chat completions endpoint |
| `completion` | Dictionary | Required | The response received from the OpenAI chat completions endpoint |
| `user_email` | String | Required | Your user email |
| `query` | String | Required | The query being asked by your user |
| `customer_id` | String | Optional | A way to identify your customer |

Here's 2 examples of using it: 

### Calling the 'raw' OpenAI API
```
from bettershot import log
import openai 

def simple_openai_call(query):
    messages = [{'role': 'user', 'content': query}]
    completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
    
            )
    log(messages=messages, completion=completion, user_email="YOUR_EMAIL", query=query, customer_id="fake_user@fake_accounts.xyz") #JUST 1 LINE OF CODE 🤯

simple_openai_call("hey! how's it going?")
```

### Calling the Langchain OpenAI API 

```
import openai
import langchain 
from bettershot import log

def simple_langchain_call(query):
    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    prompt = "You are an extremely intelligent AI assistant for BerriAI, answer all questions resepectfully and in a warm tone"
    messages = [
      SystemMessage(content=prompt),
      HumanMessage(content=query)
    ]
    result = chat(messages)
    log(messages=messages, completion=completion, user_email="YOUR_EMAIL", query=query, customer_id="fake_user@fake_accounts.xyz") #JUST 1 LINE OF CODE 🎉 

simple_langchain_call("hey! how's it going?")
```

bettershot automatically evaluates your OpenAI responses to determine if the model either invented new information (hallucination) or refused to answer ("Sorry, as an AI language model...") a user's question. 

## How does eval work?

Reliable + Fast testing is hard, and that's what we want to tackle.

Each question is evaluated 3 times. 

Each evaluation returns either True or False, along with the model's rationale for why it chose what it did. 

We pick the evaluation (True/False) that occurs most, along with the model rationale to explain reasoning. 

Each question is run in parallel and results are added to your dashboard in real-time. 

>We will be sharing the prompts soon!

## Contributing

We welcome contributions to bettershot! Feel free to create issues/PR's/or DM us (👋 Hi I'm Krrish - +17708783106)

## License

bettershot is released under the [MIT License](https://github.com/bettershot/readme/blob/master/LICENSE).
