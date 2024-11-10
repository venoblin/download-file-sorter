import os
from core.settings import get_settings
from core.utils import clean_path

def sort():
  settings = get_settings()
  downloads = os.listdir(settings['downloads'])

  for file in downloads:
    file_extension = os.path.splitext(file)[1].lower()

    if file_extension in settings['destinations']:
      file_path = clean_path(f'{settings['downloads']}/{file}')
      destination_path = settings['destinations'][file_extension]

      os.system(f'mv {file_path} {destination_path}')
