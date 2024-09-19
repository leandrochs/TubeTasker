from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ANTHROPIC_API_KEY')
client = Anthropic(api_key=API_KEY)

def get_completion_claude(new_message, message_list=[], model="claude-3-haiku-20240307"):
    message_list.append({"role": "user", "content": new_message})

    response = client.messages.create(
        model=model,
        max_tokens=1024,
        temperature=0.8,
        top_p=0.95,
        messages=message_list,
    )

    return response.content[0]
