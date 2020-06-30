"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by
in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def zero(func=None, *args):
    return func(0, *args) if func else 0


def one(func=None, *args):
    return func(1, *args) if func else 1


def two(func=None, *args):
    return func(2, *args) if func else 2


def three(func=None, *args):
    return func(3, *args) if func else 3


def four(func=None, *args):
    return func(4, *args) if func else 4


def five(func=None, *args):
    return func(5, *args) if func else 5


def six(func=None, *args):
    return func(6, *args) if func else 6


def seven(func=None, *args):
    return func(7, *args) if func else 7


def eight(func=None, *args):
    return func(8, *args) if func else 8


def nine(func=None, *args):
    return func(9, *args) if func else 9


def plus(num):
    return lambda x: x + num


def minus(num):
    return lambda x: x - num


def times(num):
    return lambda x: x * num


def divided_by(num):
    return lambda x: x // num
