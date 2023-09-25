import json
from Location.fields.common import separate_by_capital_letters

with open('Location/main4.py/cities.json') as f:
    cities = json.load(f)

with open('Location/main4.py/countries.json') as f:
    countries = json.load(f)

with open('Location/main4.py/us_states.json') as f:
    states = json.load(f)


def search_by_name(target_name, lst):
    result = list(filter(lambda item: item['name'] == target_name, lst))
    return result


def is_city(word):
    return search_by_name(word, cities) != []


def is_state(word):
    return search_by_name(word, states) != []


def is_country(word):
    return search_by_name(word, countries) != []


def get_country_for_city(city):
    if is_city(city):
        return search_by_name(city, cities)[0]['country_name']
    if is_state(city):
        return "United States"
    return None


def get_location(location):
    location = location.replace('\n', ' ')
    words = separate_by_capital_letters(location)

    for word in reversed(words):
        word = word.capitalize()
        if is_country(word):
            return word
        elif is_city(word):
            country_name = get_country_for_city(word)
            return country_name

    for i in reversed(range(len(words) - 1)):
        word = words[i].capitalize() + ' ' + words[i + 1].capitalize()
        if is_country(word):
            return word
        elif is_city(word):
            country_name = get_country_for_city(word)
            return country_name

    for i in reversed(range(len(words) - 2)):
        word = words[i].capitalize() + ' ' + words[i + 1].capitalize() + ' ' + words[i + 2].capitalize()
        if is_country(word):
            return word
        elif is_city(word):
            country_name = get_country_for_city(word)
            return country_name


def phrase_address(address):
    if type('str') != type(address) or address == 'undefined':
        raise ValueError('Field NULL')

    country = get_location(address)
    if country is None:
        raise ValueError('Not Parsable')
    return country
