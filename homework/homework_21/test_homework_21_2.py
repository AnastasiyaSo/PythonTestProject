"""Homework 21_2"""
import pytest
from homework.homework_21.test_data_21_2 import (get_valid_deposit, get_bank,
                                                 expected_amount,
                                                 get_negative_deposit,
                                                 get_invalid_deposit)
from homework import logger_module


@pytest.fixture(scope="module")
def setup_bank_and_deposit():
    """Creating and deleting banks and deposits"""
    deposit_2 = get_valid_deposit()
    bank_2 = get_bank()
    yield bank_2, deposit_2
    del deposit_2
    del bank_2


def test_calculate_deposit_amount_successfully(setup_bank_and_deposit):
    """Check that deposit amount is calculated correct"""
    bank_2, deposit_2 = setup_bank_and_deposit
    result = bank_2.method_deposit(deposit_2)
    assert round(result, 2) == expected_amount
    logger_module.logger.info("Deposit amount is %s",
                              round(deposit_2.deposit_amount, 2))


def test_negative_deposit_amount_error():
    """Check error if deposit amount is negative"""
    with pytest.raises(ValueError):
        negative_deposit = get_negative_deposit()
        bank_2 = get_bank()
        bank_2.method_deposit(negative_deposit)
    logger_module.logger.info("Deposit amount cannot be negative")


def test_invalid_deposit_amount_type_error():
    """Check error if deposit amount is invalid"""
    with pytest.raises(ValueError):
        invalid_deposit = get_invalid_deposit()
        bank_2 = get_bank()
        bank_2.method_deposit(invalid_deposit)
    logger_module.logger.info("Invalid deposit amount")
