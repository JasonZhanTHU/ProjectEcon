import pandas
import json
from Location.fields.common import separate_by_capital_letters

def is_substring(substring, main_string):
    return main_string.find(substring) != -1

def count_word_appearances(word_array):
    word_count = {}
    for word in word_array:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
def count_word_appearances(word_array):
    word_count = {}
    for word in word_array:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_count


def top_words(sorted_word_count, count):
    array = []
    for i, (word, count) in enumerate(sorted_word_count[:count]):
        array.append(word)
    return array


def save_array_to_json(array, path):
    with open(path, 'w') as file:
        json.dump(array, file, indent=' ')


df = pandas.read_excel('../main4.py/random_sample.xlsx')

tot = []
for i in range(0, 500):
    developer = df.loc[i, 'developer']
    seperated = separate_by_capital_letters(developer)
    tot += seperated

for i in range(len(tot)):
    tot[i]=tot[i].lower()

sorted_word_count = count_word_appearances(tot)

res = top_words(sorted_word_count, 100)
file_path = '../files/stop_words.json'
save_array_to_json(res, file_path)
