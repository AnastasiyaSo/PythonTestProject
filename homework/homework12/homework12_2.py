"""Homework 12"""
# Task 2
from decimal import Decimal


class Currency:
    """Creating currencies class"""
    def __init__(self, name_currency, rate_to_byn):
        self.name_currency = name_currency
        self.rate_to_byn = rate_to_byn


eur = Currency("EUR", 3.50)
usd = Currency("USD", 3.26)
byn = Currency("BYN", 1)


class Deposit:
    """Create class Deposit"""

    def __init__(self, deposit_amount, deposit_time, percent):
        self.deposit_amount = Decimal(str(deposit_amount))
        self.deposit_time = deposit_time
        self.percent = Decimal(str(percent))


class Bank:
    """Creating banks class"""
    def __init__(self, name):
        self.name = name

    def exchange_currency(self, currency_from, person_amount,
                          currency_to=byn):
        """Exchanging currency method"""
        total_amount = (person_amount * currency_from.rate_to_byn /
                        currency_to.rate_to_byn)
        return round(total_amount, 2), f"{currency_to.name_currency}"

    def method_deposit(self, deposit):
        """Calculate the amount that will be on the user's account"""
        count_of_months = 0
        while count_of_months < deposit.deposit_time:
            deposit.deposit_amount += (deposit.deposit_amount
                                       * deposit.percent / 100 / 12)
            count_of_months += 1
        print(f"Total amount: {round(deposit.deposit_amount, 2)} BYN")
        return True


class Person:
    """Creating persons class"""
    def __init__(self, currency_from, amount):
        self.currency_from = currency_from
        self.amount = amount


deposit_1 = Deposit(1000, 12, 10)
bank = Bank("Priorbank")
vasya = Person(usd, 10)
petya = Person(eur, 5)

assert bank.method_deposit(deposit_1), True
assert bank.exchange_currency(vasya.currency_from,
                              vasya.amount) == (32.60, "BYN")
assert bank.exchange_currency(petya.currency_from,
                              petya.amount) == (17.50, "BYN")

assert bank.exchange_currency(vasya.currency_from,
                              vasya.amount, eur) == (9.31, "EUR")
assert bank.exchange_currency(petya.currency_from,
                              petya.amount, usd) == (5.37, "USD")
