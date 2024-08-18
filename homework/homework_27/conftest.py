"""Fixtures"""

import pytest
from homework.homework_27 import api_requests
from homework.homework_27 import test_data
from homework.homework_27.generate_random_data import generate_email


@pytest.fixture
def request_user():
    """Fixture create user"""
    payload = {
        "name": f"{test_data.first_name} {test_data.last_name}",
        "email": generate_email(),
        "age": test_data.age,
        "phoneNumber": f"{test_data.phone}",
        "address": f"{test_data.address_number} "
                   f"{test_data.address_street} "
                   f"{test_data.address_city}",
        "role": f"{test_data.role}",
        "referralCode": f"{test_data.referral_code}"
    }
    response = api_requests.create_user_success(payload)
    test_data.id_user = response.json().get("id")
