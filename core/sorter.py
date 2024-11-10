import os
from core.settings import get_settings

def sort():
  settings = get_settings()
  downloads = os.listdir(settings['downloads'])

  for file in downloads:
    file_extension = os.path.splitext(file)[1].lower()
    
    print(file_extension)