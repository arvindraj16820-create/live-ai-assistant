import os
from dotenv import load_dotenv

load_dotenv() # loads variables from .env

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
APP_ENV = os.getenv("APP_ENV", "development")

print(f"Environment: {APP_ENV}")
print(f"API Key loaded: {'YES' if OPENAI_KEY else 'NO'}")
print("Day 1 setup complete!")