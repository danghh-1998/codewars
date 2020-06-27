"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import re


def pig_it(text):
    return ' '.join([f"{word[1:]}{word[0]}ay" if bool(re.match(r'\w+', word)) else word for word in text.split(' ')])
