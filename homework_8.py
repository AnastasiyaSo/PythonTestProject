"""My Homework 8"""

# "Task #1"


def is_increasing_sequence(sequence):
    """Check an increasing sequence"""
    sequence = tuple(sequence)
    for i in range(len(sequence)):
        temp_lst = list(sequence)
        temp_lst.pop(i)
        new_lst = sorted(list(set(temp_lst)))
        if temp_lst == new_lst:
            return True
    return False


assert (is_increasing_sequence([1, 2, 3])) is True
assert (is_increasing_sequence([1, 2, 1, 2])) is False
assert (is_increasing_sequence([1, 3, 2, 1])) is False
assert (is_increasing_sequence([1, 2, 3, 4, 5, 3, 5, 6])) is False
assert (is_increasing_sequence([40, 50, 60, 10, 20, 30])) is False


# "Task #2"


def find_opposite_number(n=10, first_number=9):
    """Find opposite number"""
    if first_number >= n/2:
        opposite_number = int(first_number - n / 2)
    else:
        opposite_number = int(n / 2 + first_number)
    return opposite_number


print(find_opposite_number())


# "Task #3"

def validate(test_numbers):
    """Validate card number"""
    sum_numbers = 0
    card_number = [int(i) for i in list(str(test_numbers))[::-1]]
    index_number = 0

    for n in card_number:
        if index_number % 2 != 0:
            n *= 2
            if n > 9:
                n = n - 9
            sum_numbers += n
        else:
            sum_numbers += n
        index_number += 1

    if sum_numbers % 10 == 0:
        return True

    return False


assert validate(4561261212345467) is True
assert validate(4561261212345464) is False
