
import re
import hashlib
import datetime

# dictionary to store users and access

users = {
    "user1": {"password":hashlib.sha256("Password1!".encode()).hexdigest(), "access_level": "admin"},
    "user2": {"password":hashlib.sha256("Password2!".encode()).hexdigest(), "access_level": "user"}
    }

# Adding more users and credentials

def create_users():
    username = input("Enter a username:")
    while True:
        try:
            password = input("Enter a password (min 8 chars, 1 uppercase, 1 special char): ")
            if len(password) < 8 or not re.search("[A-Z]", password) or not re.search("[!@#$%*&=+]", password):
                raise
            ValueError("Password does not meet requirements. Please try again")
            users[username] = {"password": hashlib.sha256(password.encode()).hexdigest(), "access_level": "user"}
            break
        except ValueError as e:
            print(e)

def authenticate_user(username, password):
    
    try:
        if username in users: # check if the username exists in the dictionary
            stored_password = users[username]["password"] # check if password matches the stored password
            input_password = hashlib.sha256(password.encode()).hexdigest()
            if input_password == stored_password:
                last_reset = users[username]["last_reset"]
                if (datetime.datetime.now() - last_reset).days  >= 30:
                    raise
                ValueError("Authentication failed. please chack your credentials and try again")
            else:
                raise ValueError('User not found.Please try again')
    except ValueError as e:
        print(e)
        return False

def reset_password(username):
    try:
        if username in users:
            password = input("Enter a new password (min 8 chars, 1 uppercase, 1 special char): ")
            if len(password) < 8 or not re.search("[A-Z]", password) or not re.search("[!@#$%*&=+]", password):
                raise
            ValueError("Password does not meet requirements. Please try again")
            users[username]["password"] = hashlib.sha256(password.encode()).hexdigest()
            users[username]["last_reset"] = datetime.datetime.now() 
            print("Password reset successfully!")
        else:
            raise ValueError("User not found. Please Try again")
    except ValueError as e:
        print(e)

