#!/home/igor/PycharmProjects/module_7/.venv/bin/python
# -*- coding: utf-8 -*-
import  os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(
           filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
