"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the
same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

"""


def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    if len(original) == len(other) == 0:
        return True
    if len(original) != len(other):
        return False
    for i in range(len(original)):
        if bool(type(original[i]) == list) != bool(type(other[i]) == list):
            return False
        elif type(original[i]) == type(other[i]) == list:
            return same_structure_as(original[i], other[i])
    return True
