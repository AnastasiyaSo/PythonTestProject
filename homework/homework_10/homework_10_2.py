"""Homework 10"""
# Task #2


def is_integer(func):
    """Function checks whether the sum of the arguments is a number"""
    def inner(a, b):
        result = func(a, b)
        if isinstance(result, (int, float)):
            return True
        return False

    return inner


@is_integer
def new_func_2(a, b):
    """Function that passes an argument"""
    return a + b


assert new_func_2(1, 2), True
assert not new_func_2("ab", "cd"), False
