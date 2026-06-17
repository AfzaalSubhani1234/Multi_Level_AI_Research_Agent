from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")



model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.2
)
