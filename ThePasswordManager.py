import subprocess
subprocess.run(["pip", "install", "cryptography"])
subprocess.run(["python", "password_vault.py"])
import json
import os
from cryptography.fernet import Fernet
from getpass import getpass
PASSWORD_FILE = "passwords.json"
KEY_FILE = "secret.key"
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

def save_passwords(data):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file)

def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

def add_password():
    account = input("Enter account name: ")
    password = getpass("Enter password: ")
    passwords = load_passwords()
    passwords[account] = encrypt(password)
    save_passwords(passwords)
    print(f"Password saved for Account : {account}!")

def get_password():
    account = input("Enter account name: ")
    passwords = load_passwords()
    if account in passwords:
        print(f"Password: {decrypt(passwords[account])}")
    else:
        print("Account not found !")

def list_accounts():
    passwords = load_passwords()
    print("\nSaved accounts:")
    for account in passwords:
        print(f"- {account}")

while True:
    print("\nThe Password Manager ->")
    print("1. Add Acount")
    print("2. Get Password")
    print("3. List My Accounts")
    print("4. Exit")

    choice = input("Choose option (1-4): ")

    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        list_accounts()
    elif choice == "4":
        print("Tata Bye-Bye!")
        break
    else:
        print("Invalid choice fool")
    def add_password():
        account = input("Enter account name: ")
        password = input("Enter password: ")
        passwords = load_passwords()
        passwords[account] = encrypt(password)
        save_passwords(passwords)
        print(f"Password saved for {account}!")