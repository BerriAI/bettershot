# bettershot 📸🚀

⚡️ A Python package for adding error monitoring to LLM Apps in a few minutes ⚡

>BetterShot by BerriAI let’s you add error (hallucinations/refusal to answer) monitoring to your LLM App in a few minutes. Like Bugsnag/Sentry for LLM apps!

## Getting Started 

bettershot automatically evaluates your OpenAI responses to determine if the model either invented new information (hallucination) or refused to answer ("Sorry, as an AI language model...") a user's question. This is useful when you want GPT to answer questions over specific data. 

To get started with bettershot, you will need to first install the library by running the following command:

`pip install bettershot`

Once installed, you can import it into your python project by running the following:

`import bettershot`

## Using bettershot

It's just 1 line of code: 

`log(messages=messages, completion=result, user_email="YOUR_EMAIL", query=query)`

Here's 2 examples of using it: 

### Calling the 'raw' OpenAI API
```from bettershot import log
import openai 

def simple_openai_call(query):
    messages = [{'role': 'user', 'content': query}]
    completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
    
            )
    log(messages=messages, completion=completion, user_email="YOUR_EMAIL", query=query) #JUST 1 LINE OF CODE!! 

simple_openai_call("hey! how's it going?")```

### Calling the Langchain OpenAI API 

```
def simple_langchain_call(query):
    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    prompt = "You are an extremely intelligent AI assistant for BerriAI, answer all questions resepectfully and in a warm tone"
    messages = [
      SystemMessage(content=prompt),
      HumanMessage(content=query)
    ]
    result = chat(messages)
    log(messages=messages, completion=completion, user_email="YOUR_EMAIL", query=query) #JUST 1 LINE OF CODE!! 

simple_langchain_call("hey! how's it going?")```

## Contributing

We welcome contributions to InstructPrompt! Feel free to create issues/PR's/or DM us (👋 Hi I'm Krrish - +17708783106)

## License

InstructPrompt is released under the [MIT License](https://github.com/instructprompt/readme/blob/master/LICENSE).
