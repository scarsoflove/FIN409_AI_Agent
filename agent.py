import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def load_prompt():
    """
    Load the system prompt from prompt.txt
    """
    with open("prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

def generate_industry_analysis(industry):

    """
    Generate Porter's Five Forces analysis
    """

    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY")
   )

    system_prompt = load_prompt()

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=f"""
    {system_prompt}

    Please analyse the following industry:

    Industry:
    {industry}

    Generate a complete Porter's Five Forces analysis.
    """
    )

    return response.text