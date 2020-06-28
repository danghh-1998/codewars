"""
Task
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API
demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
| Symbol | Value | |----------------| | I | 1 | | V | 5 | | X | 10 | | L | 50 | | C | 100 | | D | 500 | | M | 1000 |
"""


class RomanNumerals:
    sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    @staticmethod
    def to_roman(number):
        result = ''
        pointer = 0
        while number:
            div = number // RomanNumerals.num[pointer]
            number %= RomanNumerals.num[pointer]
            while div:
                result += RomanNumerals.sym[pointer]
                div -= 1
            pointer += 1
        return result

    @staticmethod
    def from_roman(roman_numeral):
        result = 0
        for idx, val in enumerate(roman_numeral):
            first_num = RomanNumerals.num[RomanNumerals.sym.index(val)]
            second_num = RomanNumerals.num[RomanNumerals.sym.index(roman_numeral[idx + 1])] if idx + 1 != len(
                roman_numeral) else -1
            if first_num >= second_num:
                result += first_num
            else:
                result -= first_num
        return result
