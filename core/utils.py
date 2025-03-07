def clean_str(str):
  new_str = ''

  for letter in str:    
    if letter == ' ':
      new_str += '\\ '
    elif letter == '(':
      new_str += '\\('
    elif letter == ')':
      new_str += '\\)'
    else:
      new_str += letter

  return new_str