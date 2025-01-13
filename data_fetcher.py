import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    response = requests.get( f"https://api.api-ninjas.com/v1/animals?name={animal_name}",
                             headers={"X-Api-Key": API_KEY} )
    if response.status_code == 200:
        return response.json()
    else:
        return []

