"""
Simple, remove the spaces from the string, then return the resultant string.
"""


def no_space(x):
    return ''.join([char for char in x if char != ' '])
