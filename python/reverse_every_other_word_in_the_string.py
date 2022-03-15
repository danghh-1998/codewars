"""
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly
one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.
"""


def reverse_alternate(string: str):
    words = [word.strip() for word in string.split(' ') if word]
    flag = False
    result = ''
    for word in words:
        result = f'{result} {word[::-1] if flag else word}'
        flag = not flag
    return result.strip()
