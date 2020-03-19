import requests
import json


def get_results(data):
    for i in range(len(data)):
        get_lexical_entries(data[i])


def get_lexical_entries(data):
    lex = data['lexicalEntries']
    for i in range(len(lex)):
        get_entry_first(lex[i])
        print(get_lexical_category(lex[i]))
        get_phrases(lex[i])


def get_entry_first(data):
    dat = ''
    try:
        dat = data['entries']
    except KeyError:
        print('no entry')
    for i in range(len(dat)):
        get_entry_second(dat[i])


def get_lexical_category(data):
    return data['lexicalCategory']['text']


def get_phrases(data):
    dat = ''
    try:
        dat = data['phrases']
    except KeyError:
        print("no phrase for this word")

    print('*'*20)
    print(' '*5, 'phrases')
    print('*'*20)
    for i in range(len(dat)):
        print(dat[i]['text'])


def get_entry_second(data):  # i'll get pronunciations from here TODO:pronunciation
    try:
        get_sense(data['senses'])
    except KeyError:
        print('no senses')


def get_sense(data):
    print('*'*20)
    print(' '*5, 'definitions')
    for i in range(len(data)):
        print(data[i]['definitions'][0])
        get_synonym(data[i])
        # print(data[i]['definitions'])


def get_synonym(data):
    dat = ''
    try:
        dat = data['synonyms']
    except KeyError:
        print('no synonym')

    print(' '*5, 'synonyms')
    print('*'*20)

    for i in range(len(dat)):
        print(dat[i]['text'])


def get_definition(word_id):
    import os
    print("*"*10 + "inside func" + "*"*10)
    print()
    print("I'm here at function start point. I'll load values in a moment..")
    app_id = os.environ.get('OXFORD_APP_ID')
    app_key = os.environ.get('OXFORD_APP_KEY')

    print(app_id, app_key)

    language = 'en-us'
    fields = 'definitions'
    strictMatch = 'false'
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + \
        '/' + word_id.lower()
    print("ok.. i see your values. i loaded them, gonna request know_>")
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    print("i requested..")
    json_data = r.json()
    print("loaded json data")
    results = json_data['results']

    print("*"*10 + "end of func" + "*"*10)

    print("\nresults:\n")
    get_results(results)  # loop 1


get_definition('incredible')
