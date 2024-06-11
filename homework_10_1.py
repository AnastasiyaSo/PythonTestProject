"""Homework 10"""
# Task #1


def validate_arguments(func):
    """Function checks whether the arguments are positive numbers"""
    def inner(*arg):
        for i in arg:
            if i <= 0:
                raise ValueError("Value is not positive")
        func(*arg)
        return True

    return inner


@validate_arguments
def new_func(*arg):
    """Function that passes an argument"""
    return arg


assert new_func(1, 4, 6), True
assert new_func(2, -5), "Value is not positive"
