"""Decorators"""


def check_status_code(expected_status_code):
    def decorator(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            assert response.status_code == expected_status_code, \
                (f"Expected status code is {expected_status_code},"
                 f" got {response.status_code}")
            return response
        return wrapper
    return decorator
