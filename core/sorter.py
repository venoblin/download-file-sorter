import os
from settings import get_settings
from utils import clean_str

def sort():
  settings = get_settings()
  downloads = os.listdir(settings['downloads'])
  file_count = 0
  
  for file in downloads:
    file_extension = os.path.splitext(file)[1].lower()

    if file_extension in settings['destinations']:
      file_count += 1
      file_path = clean_str(f"{settings['downloads']}/{file}")
      destination_path = settings['destinations'][file_extension]

      os.system(f"mv {file_path} {destination_path}")
      print(f"Moved: {file}")
      
  if file_count > 0:
    print(f"Moved {file_count} files!")
  else:
    print('No files were moved!')

def find():
  settings = get_settings()
  downloads = os.listdir(settings['downloads'])

  for file in downloads:
    if 'substring' in file:
      print(file)

find()