'''
This is a program that takes a JSON of english language words where words are Keys (all lowercase).
It then calculates the occurances of vowels being followed by another vowel or consonants,
as well as consonants being followed by another vowel or consonants.
I used the JSON file found here: https://github.com/dwyl/english-words
'''
__author__ = 'Andrew Malaty'
__email__ = 'andrew_malaty@hotmail.com'
__date__ = '2022/10/26'


import json

vowels = 'aeiouy'

current_v_next_v = 0
current_v_next_c = 0
current_c_next_v = 0
current_c_next_c = 0

# Open the JSON file and load it in.
with open('words_dictionary.json', 'r') as f:
    data = json.load(f)

# Create an array with all the words as strings
words = []
for i in data.keys():
    words.append(i)


for word in words:
    # print(word)
    for letter_index, letter in enumerate(word):
        # Check if the current letter is the last letter and break out to the next word if so.
        if letter_index == len(word) - 1:
            # print(f'{letter_index=}, {(len(word) - 1)=}')
            break
        # Check if current letter is a vowel or consonant.
        if letter in vowels:
            # print('current letter ', letter, 'next letter ', word[letter_index + 1])
            # Check if the next letter is also a vowel.
            if word[letter_index + 1] in vowels:
                current_v_next_v += 1
                # print('vv')
            else:
                current_v_next_c += 1
                # print('vc')
        else:
            # print('current letter ', letter, 'next letter ', word[letter_index + 1])
            if word[letter_index + 1] in vowels:
                current_c_next_v += 1
                # print('cv')
            else:
                current_c_next_c += 1
                # print('cc')

print()
print(f'{current_v_next_v=}, {current_v_next_c=}, {current_c_next_v=}, {current_c_next_c=}')
