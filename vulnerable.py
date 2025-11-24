# vulnerable_code.py

import hashlib

def insecure_eval(user_input):
    # Dangerous use of eval with untrusted input
    return eval(user_input)

def hardcoded_password():
    # Hardcoded password example
    password = "SuperSecret123"
    return password

def weak_hash(data):
    # Using weak MD5 hashing
    return hashlib.md5(data.encode()).hexdigest()

def division(a, b):
    # Division without handling zero division error
    return a / b

def print_user_info(name):
    # Using print instead of logging
    print(f"User name is {name}")

if __name__ == "__main__":
    data = insecure_eval("2 + 3")
    pwd = hardcoded_password()
    hashed = weak_hash("password123")
    result = division(10, 0)  # This will throw exception
    print_user_info("Alice")
