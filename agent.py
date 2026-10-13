import os
from openai import OpenAI


def load_prompt():
    """
    Load the system prompt from prompt.txt
    """
    with open("prompt.txt", "r", encoding="utf-8") as file:
        return file.read()


def generate_industry_analysis(industry):
    """
    Generate Porter Five Forces analysis
    """

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    system_prompt = load_prompt()

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"""
Please analyse the following industry:

Industry:
{industry}

Generate a complete Porter’s Five Forces analysis.
"""
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content