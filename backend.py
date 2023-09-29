import openai
import datetime
from config import apikey

# Set your OpenAI API key
openai.api_key = apikey

def provideLearningResources(ins):
    video_resources_query = f"Recommend documentation resources for learning {ins}"
    video_resources_response = chatbot_response(video_resources_query)
    
def chatbot_response(user_input):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=user_input,
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text