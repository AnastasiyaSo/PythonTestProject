"""Test data 21_2"""
from decimal import Decimal
from homework.homework_11 import homework_11_2


def get_valid_deposit():
    """Create valid deposit"""
    return homework_11_2.Deposit(10000, 24, 3)


def get_bank():
    """Create valid bank"""
    return homework_11_2.Bank()


expected_amount = Decimal('10617.57')


def get_negative_deposit():
    """Create deposit with negative amount"""
    return homework_11_2.Deposit(-1000, 12, 10)


def get_invalid_deposit():
    """Create deposit with invalid amount"""
    return homework_11_2.Deposit("invalid", 12, 10)
