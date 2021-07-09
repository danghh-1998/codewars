"""
Imagine you have a large project where is suddenly going something very messy. You are not able to guess what it is
and don't want to debug all the code through. Your project has one base class.

In this kata you will write metaclass Meta for your base class, which will collect data about all attribute accesses
and method calls in all project classes. From this data you can then better guess what is happening or which method call
is bottleneck of your app.

We will use class Debugger to store the data. Method call collection should look like this:

Debugger.method_calls.append({
    'class': ..., # class object, not string
    'method': ..., # method name, string
    'args': args, # all args, including self
    'kwargs': kwargs
})
Attribute access collection should look like this:

Debugger.attribute_accesses.append({
    'action': 'set', # set/get
    'class': ..., # class object, not string
    'attribute': ..., # name of attribute, string
    'value': value # actual value
})
You should NOT log calls of getter/setter methods that you might create by meta class.

See the tests if in doubts.
"""

from typing import Any, Tuple, Dict, List


class Subcriptable:
    def __getitem__(self, item: str):
        key = item
        if item == '_class':
            key = 'class'
        return getattr(self, key)


class MethodCall(Subcriptable):
    def __init__(self, _class: type, method: str, args: Tuple, kwargs: Dict):
        self._class = _class
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return f'<class: {self._class}, method: {self.method}, args: {self.args}, kwargs: {self.kwargs}>'


class AttributeAccessor(Subcriptable):
    def __init__(self, action: str, _class: type, attribute: str, value: Any):
        self.action = action
        self._class = _class
        self.attribute = attribute
        self.value = value

    def __repr__(self):
        return f'<class: {self._class}, action: {self.action}, attribute: {self.attribute}, value: {self.value}>'


class Debugger(object):
    method_calls: List[MethodCall] = []
    attribute_accesses: List[AttributeAccessor] = []


def func_wrapper(func_name, func):  # noqa
    def _target_func(*args, **kwargs):
        self, *_ = args
        Debugger.method_calls.append(MethodCall(_class=type(self),
                                                method=func.__name__,
                                                args=args,
                                                kwargs=kwargs))
        return func(*args, **kwargs)

    return _target_func


class Meta(type):
    def __new__(mcs, name, bases, attrs):
        def _get_attribute(self, attr):
            will_return = object.__getattribute__(self, attr)
            Debugger.attribute_accesses.append(AttributeAccessor(action='get',
                                                                 _class=type(self),
                                                                 attribute=attr,
                                                                 value=will_return))
            return will_return

        def _set_attribute(self, attr, val):
            Debugger.attribute_accesses.append(AttributeAccessor(action='set',
                                                                 _class=type(self),
                                                                 attribute=attr,
                                                                 value=val))
            object.__setattr__(self, attr, val)

        __callable = {func_name: func for func_name, func in attrs.items() if
                      not func_name.startswith('__') or func_name == '__init__'}
        for func_name, func in __callable.items():
            attrs[func_name] = func_wrapper(func_name, func)
        __new_cls = type.__new__(mcs, name, bases, attrs)
        __new_cls.__getattribute__ = _get_attribute
        __new_cls.__setattr__ = _set_attribute
        return __new_cls
