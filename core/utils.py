def clean_path(path):
  new_path = ''

  for letter in path:    
    if letter == ' ':
      new_path += '\\ '
    elif letter == '(':
      new_path += '\\('
    elif letter == ')':
      new_path += '\\)'
    else:
      new_path += letter

  return new_path