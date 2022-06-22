import re
string = input('Enter any string: ') 
new_string = re.sub(r'[^a-zA-Z0-9]','',string)
print('New string:', new_string)
