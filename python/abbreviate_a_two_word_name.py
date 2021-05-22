"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
"""


def abbrev_name(name):
    return '.'.join(word[0].upper() for word in name.split(' '))
