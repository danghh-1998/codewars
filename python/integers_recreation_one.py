"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is
itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two
elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
"""

import math


def list_squared(m, n):
    result = []
    for number in range(m, n):
        sum_square_divisors = sum(
            [i ** 2 if i == number // i else i ** 2 + (number // i) ** 2 for i in range(1, int(math.sqrt(number)) + 1)
             if not number % i])
        root = math.sqrt(sum_square_divisors)
        if root == math.floor(root):
            result.append([number, sum_square_divisors])
    return result
