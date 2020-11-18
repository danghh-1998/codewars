"""
I often find that I end up needing to write a function to return multiple values, in this case I would often split it up
into two different functions but then I have to spend time thinking of a new function name! Wouldn't it be great if I
could use same name for a function again and again...

In this kata your task is to make a decorator, FuncAdd which will allow function names to be reused and when called all
functions with that name will be called (in order) and the results returned as a tuple.

@FuncAdd
def foo():
    return 'Hello'

@FuncAdd
def foo():
    return 'World'

foo() --> ('Hello', 'World')

As well as this you will have to implement two more things, a way of deleting a particular function, and a way of
deleting all stored functions. The delete method must work as follows:

@FuncAdd
def foo():
    return 'Hello'

FuncAdd.delete(foo) # Delete all foo() functions only
foo() # Should raise NameError
And the clear method must work like this:

@FuncAdd
def foo():
    return 'Hello'

FuncAdd.clear() # Delete all decorated functions
foo() # Should raise NameError

The functions must also accept args and kwargs which would all be passed to every function.
"""


class FuncAdd:
    functions = {}

    def __init__(self, func):
        self.name = func.__name__
        if self.name not in FuncAdd.functions.keys():
            FuncAdd.functions[self.name] = []
        FuncAdd.functions[self.name].append(func)

    def __call__(self, *args, **kwargs):
        if self.name not in FuncAdd.functions.keys():
            raise NameError
        return tuple([func(*args, **kwargs) for func in FuncAdd.functions[self.name]])

    @classmethod
    def delete(cls, func):
        if func.name in FuncAdd.functions.keys():
            del cls.functions[func.name]

    @classmethod
    def clear(cls):
        cls.functions = {}
