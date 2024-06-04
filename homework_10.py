"""Homework 10"""
# Task #1


def validate_arguments(func):
    """Function checks whether the arguments are positive numbers"""
    def inner(*arg):
        for i in arg:
            if i > 0:
                continue
            raise ValueError
        func(*arg)
        return True

    return inner


@validate_arguments
def new_func(*arg):
    """Function that passes an argument"""
    return arg


assert new_func(1, 4, 6), True
assert new_func(2, -5), ValueError

# Task #2


def is_integer(func):
    """Function checks whether the sum of the arguments is a number"""
    def inner(a, b):
        c = a + b
        func(a, b)
        if isinstance(c, (int, float)):
            return True
        return f"{c} is not a number"

    return inner


@is_integer
def new_func_2(a, b):
    """Function that passes an argument"""
    return a + b


assert new_func_2(1, 2), True
assert new_func_2("ab", "cd") == "abcd is not a number"

# Task #3


def typed(_type):
    """Function transforms to one type and adds arguments"""
    def decorator(func):
        def inner(*arg):
            func(*arg)
            _str = ""
            _int = 0
            _float = 0
            if _type == str:
                for i in arg:
                    _str += str(i)
                return _str
            if _type == int:
                for i in arg:
                    _int += int(i)
                return _int
            if _type == float:
                for i in arg:
                    _float += float(i)
                return _float
            return True
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
