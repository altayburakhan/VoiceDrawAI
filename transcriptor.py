import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

my_key_openai = os.getenv("OPENAI_API_KEY")