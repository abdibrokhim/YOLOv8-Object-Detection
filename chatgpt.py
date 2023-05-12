import openai
import os
from dotenv import load_dotenv
import json


def execute(prompt: str) -> str:
    load_dotenv()

    openai.api_key = os.getenv("CHATGPT_API_KEY")

    _assistant = """

Ignore all previous instructions before this one.

Your new role is copyrighter. Your task is generating a short description around 200 characters based on the product information: name, color, brand and etc. You need to write a short description with 200 characters long, which should be understandable. You are free to use marketing key phrases to attract more visitors to buy it.

"""

    prompt_json = json.loads(prompt)

    _prompt = f"""

Product name: {prompt_json['name']}
Product color: {prompt_json['color']}

"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": _assistant},
                {"role": "user", "content": _prompt}
            ]
        )
        
        text = response['choices'][0]['message']['content'].strip()
        
        if text.endswith((".", "!", "?")):
            return text
        else:
            return text + "."
    except Exception as e:
        print(e)
        return ""


if __name__ == "__main__":
    print(execute("{\"name\": \"Macbook Air\", \"color\": \"silver\"}"))