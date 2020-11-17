"""
Consider the following expansion:

solve("3(ab)") = "ababab"     -- because "ab" repeats 3 times
solve("2(a3(b))") = "abbbabbb" -- because "a3(b)" == "abbb", which repeats twice.
Given a string, return the expansion of that string.

Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis.
There will be no letters or numbers after the last closing parenthesis.

More examples in test cases.

Good luck!
"""


def solve(st):
    arr = st.split('(')
    arr[-1] = arr[-1].replace(')', '')
    result = ''
    for item in arr[::-1]:
        result = item[:-1] + int(item[-1]) * result if item[-1].isdigit() else item + result
    return result
