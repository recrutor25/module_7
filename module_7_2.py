#!/home/igor/PycharmProjects/module_7/.venv/bin/python
# -*- coding: utf-8 -*-
import io
from pprint import  pprint
def custom_write(file_name, strings):
    strings_positions = {}
    n = 0
    file = open(file_name, 'w')
    for string in strings:
        n += 1
        key = (n, file.tell())
        file.write(f'{string}\n')
        strings_positions[key] = string
    return strings_positions
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
