"""
For a given positive integer convert it into its English representation. All words are lower case and are separated with one space. No trailing
spaces are allowed.

To keep it simple, hyphens and the writing of the word 'and' both aren't enforced. (But if you are looking for some extra challenge, such an output
will pass the tests.)

Large number reference: http://en.wikipedia.org/wiki/Names_of_large_numbers (U.S., Canada and modern British)

Input range: 1 -> 10**26 (10**16 for JS)

Examples:

int_to_english(1) == 'one'

int_to_english(10) == 'ten'

int_to_english(25161045656) == 'twenty five billion one hundred sixty one million forty five thousand six hundred fifty six'
or

int_to_english(25161045656) == 'twenty five billion one hundred sixty-one million forty-five thousand six hundred and fifty-six'
"""

units = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

dozens = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

multiples = {
    '0': '',
    '1': 'thousand',
    '2': 'million',
    '3': 'billion',
    '4': 'trillion',
    '5': 'quadrillion',
    '6': 'quintillion',
    '7': 'sextillion',
    '8': 'septillion',
    '9': 'octillion'
}


def translate(number: str):
    int_number = int(number)
    number = str(int_number)
    if int_number == 0:
        return ''
    elif int_number < 20:
        return units[number].strip()
    elif int_number < 100:
        return f'{dozens[number[0]]} {units[number[1]]}'.strip()
    elif int_number < 1000:
        return f'{units[number[0]]} hundred {translate(number=f"{number[1:]}")}'.strip()
    else:
        chunks = [number[::-1][i:i + 3][::-1] for i in range(0, len(number), 3)]
        result = ''
        for idx, val in enumerate(chunks):
            str_val = translate(val)
            result = f'{translate(val)} {multiples[str(idx)]} {result}' if str_val else result
        return result.strip()


def int_to_english(number: int):
    result = translate(number=str(number))
    print(result)
    return result
