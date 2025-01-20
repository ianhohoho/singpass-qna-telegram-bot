
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

class LLM:
    def __init__(self):
        self.client = OpenAI()

    def invoke(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return completion.choices[0].message.content
