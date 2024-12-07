#!/home/igor/PycharmProjects/module_7/.venv/bin/python
# -*- coding: utf-8 -*-

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
# есть ли необходимость в encoding если по умолчанию в системе utf-8 ?
                line = file.read().lower()
                for punkt in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(punkt, '')
                    words = line.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word_place = {}
        word = word.lower()
        for name, value in self.get_all_words().items():
            if word in value:
                word_place[name] = value.index(word) + 1

        return word_place
    def count(self, word):
        counter = {}
        word = word.lower()
        for name, value in self.get_all_words().items():
            counter[name] = value.count(word)
        return counter

finder2 = WordsFinder('test_file.txt', 'test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



