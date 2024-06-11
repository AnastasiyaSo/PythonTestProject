"""Homework 10"""
# Task #3


def typed(_type):
    """Function transforms to one type and adds arguments"""

    def decorator(func):
        def inner(*arg):
            func(*arg)
            _str = ""
            converted_args = list(map(_type, arg))
            if _type == str:
                for i in converted_args:
                    _str += str(i)
                return _str
            sum_numbers = sum(converted_args)
            return sum_numbers

        return inner

    return decorator


@typed(_type=str)
def add_str(*arg):
    """Function that passes an argument"""
    return arg


assert add_str("3", 5) == "35"
assert add_str(5, 5) == "55"
assert add_str("a", "b") == "ab"


@typed(_type=int)
def add_int(*arg):
    """Function that passes an argument"""
    return arg


assert add_int(5, 6, 7) == 18


@typed(_type=float)
def add_float(*arg):
    """Function that passes an argument"""
    return arg


assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001
