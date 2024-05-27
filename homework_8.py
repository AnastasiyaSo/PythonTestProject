"""My Homework 8"""
# "Task #1"


def solution(*args):
    """Check an increasing sequence"""
    numbers = args[0]
    index_number = 0
    numbers_of_removing = 0
    for i in numbers:

        index_number += 1

        if index_number == len(numbers) - 1:
            return True

        if i < numbers[index_number]:
            continue

        if i >= numbers[index_number]:
            numbers_of_removing += 1
            if numbers_of_removing == 2 or (index_number > 1
                                            and numbers[index_number + 1]
                                            <= numbers[index_number - 1]):
                return False
    return None


print(solution([1, 2, 3]))
print(solution([1, 2, 1, 2]))
print(solution([1, 3, 2, 1]))
print(solution([1, 2, 3, 4, 5, 3, 5, 6]))
print(solution([40, 50, 60, 10, 20, 30]))

# "Task #2"


def find_opposite_number(n=10, first_number=2):
    """Find opposite number"""
    quantity_of_numbers = len(list(range(0, n)))
    opposite_number = int(quantity_of_numbers / 2 + first_number)
    return opposite_number


print(find_opposite_number())
