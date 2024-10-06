import string
import io
class WordsFinder:
    def __init__(self, *file_names):
        self.file_name = list(file_names)
        #self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                inf = file.read().lower()
                for b in string.punctuation:
                    inf.replace(b, '')
                words = inf.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        find_ = {}
        for key, value in self.get_all_words().items():
            word = word.upper()
            if word in [x.upper() for x in value]:
                find_[key] = (value.index(word.lower()) + 1)
        return find_

    def count(self, word):
        count_ = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            count_[value] = words_count
        return count_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))