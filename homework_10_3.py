"""Homework 10"""
# Task #3


def typed(_type):
    """Function transforms to one type and adds arguments"""

    def decorator(func):
        def inner(*arg):
            converted_args = list(map(_type, arg))
            return func(*converted_args)

        return inner

    return decorator


@typed(_type=str)
def add_str(a, b):
    """Function that passes an argument"""
    return a + b


assert add_str("3", 5) == "35"
assert add_str(5, 5) == "55"
assert add_str("a", "b") == "ab"


@typed(_type=int)
def add_int(a, b, c):
    """Function that passes an argument"""
    return a + b + c


assert add_int(5, 6, 7) == 18


@typed(_type=float)
def add_float(a, b, c):
    """Function that passes an argument"""
    return a + b + c


assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001
