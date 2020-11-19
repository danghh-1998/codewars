"""
When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component
values for a color. Implement a function that meets these requirements:

Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
Returns an object with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")

"""


def hex_string_to_RGB(hex_string):
    r, g, b = [int(hex_string[i:i + 2], 16) for i in range(1, len(hex_string), 2)]
    return {'r': r, 'g': g, 'b': b}
