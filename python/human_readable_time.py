"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

"""


def make_readable(seconds):
    h_hours = str(seconds // 3600).rjust(2, '0')
    h_minutes = str(seconds % 3600 // 60).rjust(2, '0')
    h_seconds = str(seconds % 3600 % 60).rjust(2, '0')
    return f'{h_hours}:{h_minutes}:{h_seconds}'
