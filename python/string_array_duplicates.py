"""
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from
each string in the array.

For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

dup(["kelless","keenness"]) = ["keles","kenes"].

Strings will be lowercase only, no spaces. See test cases for more examples.

Good luck!

"""


def remove_dup_char(word):
    string = ''
    for char in word:
        string += char if not string or char != string[-1] else ''
    return string


def dup(arry):
    return [remove_dup_char(word) for word in arry]
