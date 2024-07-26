"""Homework # 20.2"""
import unittest
from decimal import Decimal
from homework import logger_module
from homework.homework_11 import homework_11_2


class TestBankMethods(unittest.TestCase):
    """Check  bank methods"""

    @classmethod
    def setUpClass(cls):
        cls.deposit_2 = homework_11_2.Deposit(10000, 24, 3)
        cls.bank_2 = homework_11_2.Bank()

    @classmethod
    def tearDownClass(cls):
        del cls.deposit_2
        del cls.bank_2

    def test_calculate_deposit_amount_successfully(self):
        """Check that deposit amount is calculated correct"""
        result = self.bank_2.method_deposit(self.deposit_2)
        expected_amount = Decimal('10617.57')
        self.assertAlmostEqual(result, expected_amount, places=2)
        logger_module.logger.info("Deposit amount is %s",
                                  self.deposit_2.deposit_amount)

    def test_negative_deposit_amount_error(self):
        """Check error if deposit amount is negative"""
        with self.assertRaises(ValueError):
            self.deposit_3 = homework_11_2.Deposit(-1000, 12, 10)
            self.bank_2.method_deposit(self.deposit_3)
        logger_module.logger.info("Deposit amount cannot be negative")

    def test_invalid_deposit_amount_type_error(self):
        """Check error if deposit amount is invalid"""
        with self.assertRaises(ValueError):
            self.deposit_4 = homework_11_2.Deposit("invalid", 12, 10)
            self.bank_2.method_deposit(self.deposit_4)
        logger_module.logger.info("Invalid deposit amount")
