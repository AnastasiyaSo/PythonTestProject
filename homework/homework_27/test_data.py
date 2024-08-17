"""Test data"""

from homework.homework_27.generate_random_data import (generate_string,
                                                       generate_email,
                                                       generate_age,
                                                       generate_phone,
                                                       generate_int,
                                                       generate_role)

token = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMD"
         "Y3MzM4NTEyNjIxNTc0MzQyNDQiLCJpYXQiOjE3MjM5MjA5OTYsImV4cC"
         "I6MTcyMzkyNDU5Nn0.1Eh6O7RUdpuZ98JarEyWM3psXJ5MnPon7KjW2Q7aGEY")

base_url = "https://alexqa.netlify.app/.netlify/"
endpoint_1 = "functions/createUser"
endpoint_2 = "functions/getUser/"
endpoint_3 = "functions/getUsers/"
endpoint_4 = "functions/updateUser/"
endpoint_5 = "functions/deleteUser/"
endpoint_6 = "functions/checkUserStatus/"

first_name = generate_string(3, 6)
last_name = generate_string(4, 8)
email = generate_email()
invalid_email = generate_string(4, 8)
age = generate_age()
phone = generate_phone()
invalid_phone = generate_int()
address_number = generate_int()
address_street = generate_string(4, 10)
address_city = generate_string(4, 10)
role = generate_role()
invalid_role = generate_string(3, 6)
referral_code = generate_string(8, 8)

id_user = None
invalid_id_user = generate_int()

get_users_keys = {"users", "totalPages"}
