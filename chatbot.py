from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL_NAME
from prompts import BASE_PROMPT, SHOES_RULE, BELTS_RULE

openai = OpenAI(api_key=OPENAI_API_KEY)

def build_system_message(user_message: str) -> str:
    system_message = BASE_PROMPT + SHOES_RULE
    if "belt" in user_message:
        system_message += BELTS_RULE
    return system_message


def chat(message, history):
    messages = (
        [{"role": "system", "content": build_system_message(message)}]
        + history
        + [{"role": "user", "content": message}]
    )

    stream = openai.chat.completions.create(
        model=OPENAI_MODEL_NAME, messages=messages, stream=True
    )

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response
