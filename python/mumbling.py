"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(string):
    return '-'.join(
        [''.join(
            [''.join(
                [char.upper(), *[char.lower() for _ in range(idx)]]
            ) for char in word]
        ) for idx, word in enumerate(string)])
