"""API requests methods"""

import requests
from homework.homework_27 import test_data
from homework.homework_27.decorators import check_status_code


@check_status_code(200)
def create_user_success(payload):
    """Create user success function"""
    full_url = f"{test_data.base_url}functions/createUser"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.post(full_url, headers=headers, json=payload)
    return response


@check_status_code(400)
def create_user_failure(payload):
    """Create user failure function"""
    full_url = f"{test_data.base_url}functions/createUser"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.post(full_url, headers=headers, json=payload)
    return response


@check_status_code(200)
def get_user_success(user_id):
    """Get user success function"""
    full_url = f"{test_data.base_url}functions/getUser/{user_id}"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.get(full_url, headers=headers)
    return response


@check_status_code(400)
def get_user_failure(invalid_id_user):
    """Get user failure function"""
    full_url = (f"{test_data.base_url}functions/getUser/"
                f"{invalid_id_user}")
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.get(full_url, headers=headers)
    return response


@check_status_code(200)
def get_users():
    """Get users success function"""
    full_url = f"{test_data.base_url}functions/getUsers/"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.get(full_url, headers=headers)
    return response


@check_status_code(200)
def update_user_success(user_id, payload):
    """Update user success function"""
    full_url = f"{test_data.base_url}functions/updateUser/{user_id}"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.put(full_url, headers=headers, json=payload)
    return response


@check_status_code(400)
def update_user_failure(user_id, payload):
    """Get users failure function"""
    full_url = f"{test_data.base_url}functions/updateUser/{user_id}"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.put(full_url, headers=headers, json=payload)
    return response


@check_status_code(404)
def delete_user(user_id):
    """Delete users success function"""
    full_url = f"{test_data.base_url}functions/deleteUser/{user_id}"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.delete(full_url, headers=headers)
    return response


@check_status_code(200)
def check_status(user_id):
    full_url = f"{test_data.base_url}functions/checkUserStatus/{user_id}"
    headers = {"Authorization": f"Bearer {test_data.token}"}
    response = requests.get(full_url, headers=headers)
    return response
