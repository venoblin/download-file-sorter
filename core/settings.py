import os
import json

def get_settings():
  dir_path = os.path.dirname(os.path.abspath(__file__))

  with open(f'{dir_path}/../settings.json', 'r') as file:
    data = json.load(file)

  return data
