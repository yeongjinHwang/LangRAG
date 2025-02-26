import json
import os 
from openai import OpenAI


with open("config.json", "r") as f: 
    config = json.load(f)

api_key = config.get("api")

client = OpenAI(api_key=api_key)
response = client.models.list()

for model in response.data:
    if model.id.startswith("gpt-4"):
        print(model.id)