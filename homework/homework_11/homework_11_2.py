"""Homework # 11"""
# Task #2

from decimal import Decimal, InvalidOperation


class Deposit:
    """Create class Deposit"""

    def __init__(self, deposit_amount, deposit_time, percent):
        try:
            self.deposit_amount = Decimal(str(deposit_amount))
        except InvalidOperation as exc:
            raise ValueError("Invalid deposit amount") from exc
        if self.deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.deposit_time = deposit_time
        self.percent = Decimal(str(percent))


class Bank:
    """Create class Bank"""

    def method_deposit(self, deposit):
        """Calculate the amount that will be on the user's account"""
        count_of_months = 0
        while count_of_months < deposit.deposit_time:
            deposit.deposit_amount += (deposit.deposit_amount
                                       * deposit.percent / 100 / 12)
            count_of_months += 1
        # print(f"Total amount: {round(deposit.deposit_amount, 2)} BYN")
        return round(deposit.deposit_amount, 2)


if __name__ == "__main__":
    deposit_1 = Deposit(1000, 12, 10)
    bank_1 = Bank()

    assert bank_1.method_deposit(deposit_1) == Decimal("1220.39")
