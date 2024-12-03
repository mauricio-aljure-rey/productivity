# This script converts strings to Morse code
# All characters are turned to a-z, 0-9. Others are ignored.

import json
import unicodedata
import re


def load_morse_dict():
    with open('morse_map.json', 'r') as f:
        morse_dict = json.load(f)
    return morse_dict

def to_morse(data):
    # Converting all characters to english characters
    data = unicodedata.normalize('NFD', data)

    # Turning all letters to upper letters
    data = data.upper()

    # Removing non numeric or letter characters
    data = re.sub("[^A-Z 0-9]", "", data)
    # print(f'The string to convert to Morse is:\n{data}')

    # Translating into morse code
    morse_dict = load_morse_dict()
    translated = ''
    try:
        for item in data:
            if item == ' ':
                translated += '       ' # 7 spaced between words
            else:
                translated += morse_dict[item] + '   ' # morse key + 3xspace
        return translated
    except:
        print('String given cannot be translated')


if __name__ == "__main__":
    data = 'Hello world! SOS!'
    morse_data = to_morse(data)
    print(morse_data)
