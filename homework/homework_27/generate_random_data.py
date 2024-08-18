"""Generate random data"""

import random
import string


def generate_string(min_length, max_length):
    """Random string"""
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_int():
    """Random int"""
    number = random.randint(1, 999)
    return number


def generate_email():
    """Random email"""
    domains = ["example.com", "test.com", "mail.com"]
    return f"{generate_string(4, 10)}@{random.choice(domains)}"


def generate_age():
    """Random age"""
    age = random.randint(18, 99)
    return age


def generate_phone():
    """Random phone"""
    return f"+{random.randint(10000000000, 99999999999)}"


def generate_role():
    """Random role"""
    role = random.choice(["user", "admin", "moderator"])
    return f"{role}"
