
import os
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# Using OpenAI's API instead if available
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY:
    llm_config = {
        "config_list": [
            {
                "model": "gpt-4o",
                "api_key": OPENAI_API_KEY
            }
        ],
        "temperature": 0.1
    }
else:
   llm_config = {
    "config_list": [
        {
            "model": "llama-3.3-70b-versatile",  # Using Llama 3 70B through Groq
            "api_key": GROQ_API_KEY,
            "base_url": "https://api.groq.com/openai/v1",
            "price": [0.0001, 0.0001]  # Add custom pricing to avoid the warning    
        },
        {
            "model": "llama3-70b-8192",  # Using Llama 3 70B through Groq
            "api_key": GROQ_API_KEY,
            "base_url": "https://api.groq.com/openai/v1",
            "price": [0.0001, 0.0001]  # Add custom pricing to avoid the warning    
        }
    ],
    "temperature": 0.2,  # Low temperature for more deterministic outputs
    "timeout": 120,
    "cache_seed": None  # No caching for fresh results
}