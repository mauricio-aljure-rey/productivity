# NATO alphabet project. A spelling aid for words
# Taken from online course

import pandas

alp = pandas.read_csv("nato_phonetic_alphabet.csv")

word = input("Enter word to decode: ").upper()
word = [k for k in word]

word_decoded = [''.join(alp[alp.letter == word_letter].code.values) for word_letter in word]

print(word_decoded)