'''
This is a program that takes a JSON of english language words where words are Keys (all lowercase).
It then calculates the occurances of vowels and consonants.
I used the JSON file found here: https://github.com/dwyl/english-words
'''
__author__ = 'Andrew Malaty'
__email__ = 'andrew_malaty@hotmail.com'
__date__ = '2022/10/26'


import json

vowels = 'aeiouy'

v = 0
c = 0

# Open the JSON file and load it in.
with open('words_dictionary.json', 'r') as f:
    data = json.load(f)

# Create a string with all the words in it
all_words = ''
for i in data.keys():
    all_words += i

# Count the number of vowels
for i in all_words:
    if i in vowels:
        v += 1
c = len(all_words) - v

print(f'{v=}, {c=}')
