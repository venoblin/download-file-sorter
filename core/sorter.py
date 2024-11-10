import os
from core.settings import get_settings

def sort():
  settings = get_settings()
  downloads = os.listdir(settings['downloads'])

  print(downloads)