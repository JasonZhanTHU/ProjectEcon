import json
import sys
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')
from Location.fields.common import separate_by_capital_letters
from stanfordcorenlp import StanfordCoreNLP
from nltk.corpus import words

nlp = StanfordCoreNLP(r'../../../Location/stanford-corenlp-4.5.4', lang='en')
english_words = set(words.words())

with open('../../../Location/files/stop_words.json') as f:
    stop_words = json.load(f)


def is_english_word(word):
    return word.lower() in english_words or word.lower() in stop_words


with open('../../../Location/files/stop_words.json') as f:
    stop_words = json.load(f)


def identify_through_name(developer):
    words = separate_by_capital_letters(developer)
    if len(words) == 1:
        return 1
    for word in words:
        if len(word) == 1:
            continue
        if is_english_word(word):
            return 1
        if word in stop_words:
            return 1
    return 0


def identify_through_ner(developer):
    doc = nlp.ner(developer)
    flag = 0
    for i in range(len(doc)):
        if doc[i][1] != 'PERSON':
            flag = 1
    return flag
