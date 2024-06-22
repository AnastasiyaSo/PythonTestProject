"""Homework 14"""
# Task # 2


def calculator(data):
    """Function performs calculations and processes exceptions"""

    try:
        output_data = addition_and_subtraction(
            multiplication_and_division(
                exponentiation(data)))

        return output_data

    except ZeroDivisionError:
        print("ZeroDivisionError")

    except ValueError:
        print("ValueError")

    except IndexError:
        print("IndexError")

    return None


def exponentiation(data):
    """Function performs exponentiation"""
    operations = data.split()
    while "**" in operations:
        for i in range(len(operations) - 1):
            if operations[i] == "**":
                a = int(operations[i - 1])
                b = int(operations[i + 1])
                operations[i - 1] = str(a ** b)
                operations.pop(i)
                operations.pop(i)
                break
    return operations


def multiplication_and_division(operations):
    """Function performs multiplication and division"""
    while "*" in operations or "/" in operations:
        for i in range(len(operations) - 1):
            if operations[i] == "*":
                a = float(operations[i - 1])
                b = float(operations[i + 1])
                operations[i - 1] = str(a * b)
                operations.pop(i)
                operations.pop(i)
                break

            if operations[i] == "/":
                a = float(operations[i - 1])
                b = float(operations[i + 1])
                operations[i - 1] = str(a / b)
                operations.pop(i + 1)
                operations.pop(i)
                break
    return operations


def addition_and_subtraction(operations):
    """Function performs addition and subtraction"""
    while "+" in operations or "-" in operations:
        for i in range(len(operations) - 1):
            if operations[i] == "+":
                a = float(operations[i - 1])
                b = float(operations[i + 1])
                operations[i - 1] = str(a + b)
                operations.pop(i)
                operations.pop(i)
                break

            if operations[i] == "-":
                a = float(operations[i - 1])
                b = float(operations[i + 1])
                operations[i - 1] = str(a - b)
                operations.pop(i)
                operations.pop(i)
                break
    return operations[0]


print(calculator(data=input("~ ")))
