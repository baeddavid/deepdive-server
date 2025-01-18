import backoff
import openai

openai.organization = "key"
openai.api_key = "key"

@backoff.on_exception(backoff.expo, openai.OpenAIError)
def complete_prompt(prompt, **kwargs):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(messages=messages, **kwargs)
    return response.choices[0].message.content
