
import os
import json

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate


# Load the Hugging Face token from .env
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")


# Connect to Hugging Face
client = InferenceClient(
    api_key=HF_TOKEN
)


# LangChain prompt
prompt = PromptTemplate.from_template("""
You are an AI assistant for a Smart Plant Care Advisor.

Read the user's natural-language description of a plant.

Your job is to understand the description and extract:

1. plant_name
2. soil_moisture as a number from 0 to 100
3. temperature as a number from 0 to 40
4. light as a number from 0 to 100

Use reasonable estimates when the user uses descriptive words.

Examples:

dry soil = 20
slightly dry soil = 35
moist soil = 55
wet soil = 85

low sunlight = 20
moderate sunlight = 50
bright sunlight = 85

cold = 12
cool = 18
warm = 25
hot = 35

Return ONLY valid JSON.

Do not add explanations.
Do not add markdown.
Do not use ```.

Use exactly this format:

{{
    "plant_name": "Tomato",
    "soil_moisture": 20,
    "temperature": 32,
    "light": 85
}}

User description:

{user_input}
""")


def extract_plant_data(user_input):

    # LangChain creates the final prompt
    formatted_prompt = prompt.format(
        user_input=user_input
    )

    # Send the prompt to the Hugging Face conversational model
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:fastest",
        messages=[
            {
                "role": "user",
                "content": formatted_prompt
            }
        ],
        max_tokens=300,
        temperature=0.1
    )

    # Get the AI response
    text = response.choices[0].message.content.strip()

    # Remove accidental markdown formatting
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Convert AI JSON into Python data
    data = json.loads(text)

    return data