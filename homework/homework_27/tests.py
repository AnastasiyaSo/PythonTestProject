"""Tests"""

import pytest
from homework.homework_27 import api_requests
from homework.homework_27 import test_data
from homework import logger_module


def test_create_user_success():
    """Test create user success"""
    payload = {
        "name": f"{test_data.first_name} {test_data.last_name}",
        "email": f"{test_data.email}",
        "age": test_data.age,
        "phoneNumber": f"{test_data.phone}",
        "address": f"{test_data.address_number} {test_data.address_street}"
                   f" {test_data.address_city}",
        "role": f"{test_data.role}",
        "referralCode": f"{test_data.referral_code}"
    }
    response = api_requests.create_user_success(payload)
    assert response.json().get("name") == (f"{test_data.first_name} "
                                           f"{test_data.last_name}")
    assert response.json().get("email") == test_data.email
    assert response.json().get("age") == test_data.age
    assert response.json().get("phoneNumber") == test_data.phone
    assert response.json().get("address") == (f"{test_data.address_number}"
                                              f" {test_data.address_street}"
                                              f" {test_data.address_city}")
    assert response.json().get("role") == test_data.role
    assert response.json().get("referralCode") == test_data.referral_code
    assert response.json().get("status") == "created"
    logger_module.logger.info("Test create user success")


def test_create_user_invalid_email():
    """Test create user invalid email"""
    payload = {
        "name": f"{test_data.first_name} {test_data.last_name}",
        "email": f"{test_data.invalid_email}",
        "age": test_data.age,
        "phoneNumber": f"{test_data.phone}",
        "address": f"{test_data.address_number} {test_data.address_street}"
                   f" {test_data.address_city}",
        "role": f"{test_data.role}",
        "referralCode": f"{test_data.referral_code}"
    }
    response = api_requests.create_user_failure(payload)
    assert response.json().get("error") == "Invalid email address"
    logger_module.logger.info("Test create user invalid email success")


def test_create_user_invalid_phone():
    """Test create user invalid phone"""
    payload = {
        "name": f"{test_data.first_name} {test_data.last_name}",
        "email": f"{test_data.email}",
        "age": test_data.age,
        "phoneNumber": f"{test_data.invalid_phone}",
        "address": f"{test_data.address_number} {test_data.address_street}"
                   f" {test_data.address_city}",
        "role": f"{test_data.role}",
        "referralCode": f"{test_data.referral_code}"
    }
    response = api_requests.create_user_failure(payload)
    assert response.json().get("error") == ("Invalid phone number:"
                                            " it must be in the format"
                                            " +<country code> followed by"
                                            " 7 to 10 digits")
    logger_module.logger.info("Test create user invalid phone success")


def test_create_user_invalid_role():
    """Test create user invalid role"""
    payload = {
        "name": f"{test_data.first_name} {test_data.last_name}",
        "email": f"{test_data.email}",
        "age": test_data.age,
        "phoneNumber": f"{test_data.phone}",
        "address": f"{test_data.address_number} {test_data.address_street}"
                   f" {test_data.address_city}",
        "role": f"{test_data.invalid_role}",
        "referralCode": f"{test_data.referral_code}"
    }
    response = api_requests.create_user_failure(payload)
    assert response.json().get("error") == ("Invalid role: it must be"
                                            " one of \"user\", \"admin\","
                                            " or \"moderator\"")
    logger_module.logger.info("Test create user invalid role success")


def test_get_user_success(request_user):
    """Test get user success"""
    response = api_requests.get_user_success(test_data.id_user)
    assert response.json().get("id") == f"{test_data.id_user}"
    logger_module.logger.info("Test get user success")


def test_get_user_invalid_id():
    """Test get user invalid id"""
    response = api_requests.get_user_failure(test_data.invalid_id_user)
    assert response.json().get("error") == "Invalid User ID format"
    logger_module.logger.info("Test get user invalid id success")


def test_get_list_users_success():
    """Test get list users success"""
    response = api_requests.get_users()
    assert response.json().keys() == test_data.get_users_keys
    logger_module.logger.info("Test get list users success")


def test_update_user_success(request_user):
    """Test update user success"""
    payload = {
        "name": f"{test_data.first_name} {test_data.last_name}",
        "email": f"{test_data.email}",
        "age": test_data.age,
        "phoneNumber": f"{test_data.phone}",
        "address": f"{test_data.address_number} {test_data.address_street}"
                   f" {test_data.address_city}",
        "role": f"{test_data.role}",
        "referralCode": f"{test_data.referral_code}"
    }
    response = api_requests.update_user_success(test_data.id_user, payload)
    assert response.json().get("name") == (f"{test_data.first_name}"
                                           f" {test_data.last_name}")
    assert response.json().get("email") == test_data.email
    assert response.json().get("age") == test_data.age
    assert response.json().get("phoneNumber") == test_data.phone
    assert response.json().get("address") == (f"{test_data.address_number}"
                                              f" {test_data.address_street}"
                                              f" {test_data.address_city}")
    assert response.json().get("role") == test_data.role
    assert response.json().get("referralCode") == test_data.referral_code
    assert response.json().get("status") == "updated"
    logger_module.logger.info("Test update user success")


def test_update_user_invalid_id():
    """Test update user invalid id"""
    payload = {
        "name": f"{test_data.first_name} {test_data.last_name}",
        "email": f"{test_data.email}",
        "age": test_data.age,
        "phoneNumber": f"{test_data.phone}",
        "address": f"{test_data.address_number} "
                   f"{test_data.address_street} "
                   f"{test_data.address_city}",
        "role": f"{test_data.role}",
        "referralCode": f"{test_data.referral_code}"
    }
    response = api_requests.update_user_failure(test_data.invalid_id_user,
                                                payload)
    assert response.json().get("error") == "Invalid User ID format"
    logger_module.logger.info("Test update user invalid id success")


def test_update_user_incorrect_body(request_user):
    """Test update user incorrect body"""
    payload = "incorrect body"
    response = api_requests.update_user_failure(test_data.id_user, payload)
    assert response.json().get("error") == ("At least one field is "
                                            "required for update")
    logger_module.logger.info("Test update user incorrect body success")


@pytest.mark.xfail(reason="404 Not Found 'error':'Order not found'")
def test_delete_user_success(request_user):
    """Test delete user success"""
    response = api_requests.delete_user(test_data.id_user)
    assert response.json().get("id") == f"{test_data.id_user}"
    assert response.json().get("status") == "deleted"
    logger_module.logger.info("Test delete user success")


def test_check_user_status_success(request_user):
    """Test check user status success"""
    response = api_requests.check_status(test_data.id_user)
    assert response.json().get("id") == f"{test_data.id_user}"
    assert response.json().get("name") == (f"{test_data.first_name}"
                                           f" {test_data.last_name}")
    assert response.json().get("status") == "created"
    logger_module.logger.info("Test check user status success")
