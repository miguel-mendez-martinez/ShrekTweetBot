import os
from dotenv import load_dotenv

load_dotenv()

#creacion de la estructura que contiene los diferentes datos sobre la APY
CREDENTIALS = {
  'API_KEY': os.environ['API_KEY'],
  'API_SECRET': os.environ['API_SECRET'],
  'ACCESS_KEY': os.environ['ACCESS_KEY'],
  'ACCESS_SECRET': os.environ['ACCESS_SECRET']
}