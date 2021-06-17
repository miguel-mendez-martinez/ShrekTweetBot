import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS = {
  'API_KEY': os.environ['API_KEY'],
  'API_SECRET': os.environ['API_SECRET'],
  'ACCESS_KEY': os.environ['ACCESS_KEY'],
  'ACCESS_SECRET': os.environ['ACCESS_SECRET']
}