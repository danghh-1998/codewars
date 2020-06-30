"""
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger),
and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in
integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been
simplified in the following way ( -> means application of simplify):

All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
"cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


All monomials appears in order of increasing number of variables, e.g.:
"-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
"a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

There is no leading + sign if the first coefficient is positive, e.g.:
"-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so
you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english
alphabet.
"""

import re


def simplify(poly):
    monomials = [re.search(r'([+-]?\d*)([a-z]+)', monomial).groups() for monomial in re.findall(r'[+-]?\w+', poly)]
    sorted_monomials = sorted([[int(monomial[0] if monomial[0] not in ['+', '-'] else f"{monomial[0]}1") if monomial[
        0] else 1, ''.join(sorted(monomial[1]))] for monomial in monomials],
                              key=lambda monomial: (len(monomial[1]), monomial[1]))
    abridged_monomials = []
    for monomial in sorted_monomials:
        if abridged_monomials and monomial[1] == abridged_monomials[-1][1]:
            abridged_monomials[-1][0] += monomial[0]
        else:
            abridged_monomials.append(monomial)
    result = ''
    for monomial in abridged_monomials:
        if monomial[0] == -1:
            result += f"-{monomial[1]}"
        elif monomial[0] < -1:
            result += f"{str(monomial[0])}{monomial[1]}"
        elif monomial[0] == 1:
            result += f"+{monomial[1]}"
        elif monomial[0] > 1:
            result += f"+{str(monomial[0])}{monomial[1]}"
    return result[1:] if result[0] == '+' else result
