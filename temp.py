import json

import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
data = {'list': [13, 424, 35.141, 1337, 'help'],
        'string': 'braun',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 34}}

with io.open('information.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

with open('information.json') as data_file:
    data_loaded = json.load(data_file)

print(data == data_loaded)

    
  
  
  
