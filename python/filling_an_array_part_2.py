"""
Following on from Part 1, part 2 looks at some more complicated array contents.

So let's try filling an array with...

...square numbers
The numbers from 1 to n*n

const squares = n => ???
squares(5) // [1, 4, 9, 16, 25]
...a range of numbers
A range of numbers starting from start and increasing by step

const range = (n, start, step) => ???
range(6, 3, 2) // [3, 5, 7, 9, 11, 13]
...random numbers
A bunch of random integers between min and max

const random = (n, min, max) => ???
random(4, 5, 10) // [5, 9, 10, 7]
...prime numbers
All primes starting from 2 (obviously)...

const primes = n => ???
primes(6) // [2, 3, 5, 7, 11, 13]
HOTE: All the above functions should take as their first parameter a number that determines the length of the returned
array.

"""

import math
import random


def squares(n):
    return [i ** 2 for i in range(1, n + 1)]


def num_range(n, start, step):
    return [start + i * step for i in range(n)]


def rand_range(n, mn, mx):
    return [random.randint(mn, mx) for _ in range(n)]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes(n):
    result = []
    i = 2
    while len(result) < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result
