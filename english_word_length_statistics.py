'''
This is a program that takes a JSON of english language words where words are Keys (all lowercase).
It then calculates the mean, standard deviation, and a few other statistics about word lengths.
I used the JSON file found here: https://github.com/dwyl/english-words
'''
__author__ = 'Andrew Malaty'
__email__ = 'andrew_malaty@hotmail.com'
__date__ = '2022/10/26'

import json
import math

# Open the JSON file and load it in.
with open('words_dictionary.json', 'r') as f:
    data = json.load(f)

# Make an array of all the word lengths
word_lengths = []
for i in data.keys():
    word_lengths.append(len(i))
print(f'max={max(word_lengths)}')
print(f'min={min(word_lengths)}')
mean = sum(word_lengths) / len(word_lengths)

# Make an array of the variances
variance = word_lengths
for j, k in enumerate(word_lengths):
    variance[j] = k - mean

# Calculate the standard deviation
std_dev = 0
for m in variance:
    std_dev += m**2
std_dev = math.sqrt(std_dev / (len(variance)))

print(f'{mean=}')
print(f'{std_dev=}')
