"""Homework 14"""
# Task # 2


def calculate(data):
    """Calculate function"""
    try:
        operations = data.split()

        while len(operations) > 1:
            for i in range(len(operations) - 1):
                if operations[i] == "**":
                    a = int(operations[i - 1])
                    b = int(operations[i + 1])
                    operations[i - 1] = str(a ** b)
                    operations.pop(i)
                    operations.pop(i)
                    break

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

    except ZeroDivisionError:
        print("ZeroDivisionError")

    except ValueError:
        print("ValueError")

    except IndexError:
        print("IndexError")

    return None

print(calculate(data=input("~ ")))
