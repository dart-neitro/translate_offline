"""
load english - russian dictionary
from file to mongo db
"""
import re

from application.app.core.db_utils import MongoDB

import config

text = ''
with open('data/Mueller24.koi', "rb") as f:
    text = f.read()

text = text.decode(encoding='koi8-r')

split_text = text.split('\n')

about_dictionary = ''

line = split_text.pop(0)
while line.strip().startswith('(C)'):
    about_dictionary += line + '\n'
    line = split_text.pop(0)

reference_words = []

any_word = '[a-z|A-Z|а-я|А-я|-]+'
english_part = '[a-z|A-Z|()\- ]+'
russian_part = '[а-я|А-я|()\-  ]+'

pattern = '_({})[.|:] ({}) ({})'.format(any_word, english_part, russian_part)

while line.strip().startswith('_'):
    try:

        line = ' '.join(line.split())
        data = re.findall(pattern, line)
        reference_words.append(dict(zip(['key', 'eng', 'rus'], data[0])))

    except:
        print('FATALL ERROR in <<< %s >>>' % line)
    finally:
        line = split_text.pop(0)


# TODO update code bellow
while not line.startswith('a bit'):
    line = split_text.pop(0)

pattern_simple = '({}) ({})'.format(english_part, russian_part)


keyword = '([a-z|A-Z|()\- ]+) '
abbreviation = '(_[a-z|A-Z|а-я|А-я|-]+.)?[ ]?'
description = '([a-z|A-Z|а-я|А-я|0-9|\(\)\-,;._ ]+)$'
description = '(.*)$'

pattern_extra = '{}{}{}'.format(
    keyword, abbreviation, description)

results = []

errors = []
# render dictionary
while True:
    try:

        line = ' '.join(line.split())
        if re.findall(pattern_extra, line):
            # print(line)
            data = re.findall(pattern_extra, line)
            record = dict(zip(
                ['key', 'key_extra', 'translate'], data[0]))
            results.append(record)

        else:
            errors.append(line)

        line = split_text.pop(0)
    except IndexError:
        break
    except:
        print('FATALL ERROR in <<< %s >>>' % line)
        line = split_text.pop(0)

if config.MONGODB_HOST and config.MONGODB_PORT:
    client = MongoDB(config.MONGODB_HOST, config.MONGODB_PORT)
else:
    client = MongoDB()


words = client.get_collection('translate_offline', 'words')
words.insert(results)

print('errors =', len(errors))
print('results =', len(results))

print('The end!')
