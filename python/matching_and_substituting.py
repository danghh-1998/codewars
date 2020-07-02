"""
I got lots of files beginning like this:

Program title: Primes
Author: Kern
Corporation: Gold
Phone: +1-503-555-0091
Date: Tues April 9, 2005
Version: 6.7
Level: Alpha

Here we will work with strings like the string data above and not with files.

The function change(s, prog, version) given:
s=data, prog="Ladder" , version="1.1" will return:
"Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1"

Rules:
- The date should always be "2019-01-01".
- The author should always be "g964".
- Replace the current "Program Title" with the prog argument supplied to your function. Also remove "Title",
  so in the example case "Program Title: Primes" becomes "Program: Ladder".
- Remove the lines containing "Corporation" and "Level" completely.
- Phone numbers and versions must be in valid formats.
- A valid version in the given string data is one or more digits followed by a dot, followed by one or more digits.
  So 0.6, 5.4, 14.275 and 1.99 are all valid, but versions like .6, 5, 14.2.7 and 1.9.9 are invalid.
- A valid phone format is +1-xxx-xxx-xxxx, where each x is a digit.
- If the phone or version format is not valid, return "ERROR: VERSION or PHONE".
- If the version format is valid and the version is anything other than 2.0, replace it with the version parameter
  supplied to your function. If it’s 2.0, don’t modify it.
- If the phone number is valid, replace it with "+1-503-555-0090".
"""

import re


def change(s, prog, version):
    regex = 'Program title: (.+)\\nAuthor: (.+)\\nCorporation: (.+)\\nPhone: (.+)\\nDate: (.+)\\nVersion: (' \
            '.+)\\nLevel: (.+) '
    title, author, corporation, phone, date, ver, level = re.findall(regex, s)[0]
    version_regex = '^\d+\.\d+$'
    if not re.findall(version_regex, ver):
        return "ERROR: VERSION or PHONE"
    if ver != '2.0':
        ver = version
    phone_regex = '\+1\-\d{3}\-\d{3}\-\d{4}'
    if not re.findall(phone_regex, phone):
        return "ERROR: VERSION or PHONE"
    phone = '+1-503-555-0090'
    date = '2019-01-01'
    return f"Program: {prog} Author: g964 Phone: {phone} Date: {date} Version: {ver}"
