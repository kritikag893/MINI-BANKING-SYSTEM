# calling the hashlib module to hash the PIN for security purposes.
# importing the save_accounts function from storage.py file to save the accounts to the json file.
# importing the valid_acc_no, valid_pin, and valid_amt functions from
#  validation.py file to validate the account number, PIN, and amount respectively.
import hashlib
from storage import save_accounts
from validation import valid_acc_no, valid_pin, valid_amt


def create_acc(accounts):
    print("\n-----Create Account-----")

    name = input("Enter account holder name: ")

    while True:
        account_no = input("Enter 8-digit account number: ")

        if valid_acc_no(account_no):
            if account_no in accounts:
                print("Account number already exists. Please try again.")
            else:
                break
        else:
            print("Invalid account number. Please enter an 8-digit account number.")

    while True:
        pin = input("Enter 4-digit PIN: ")

        if valid_pin(pin):
            # hashing the PIN using SHA-256 algorithm for security purposes.
            pin_hash = hashlib.sha256(pin.encode()).hexdigest()
            # breaking the loop if the PIN is valid and hashed.
            break
        else:
            print("Invalid PIN. Please enter a 4-digit PIN.")

    while True:
        try:
            balance = float(input("Enter initial balance: "))

            if valid_amt(balance):
                break
            else:
                print("Initial balance cannot be negative.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

## creating a new account in the accounts dictionary with the account number as the key and
#  a dictionary containing the account holder name, hashed PIN, initial balance, and
#  an empty list for transactions as the value.
    accounts[account_no] = {
        "name": name,
        "pin": pin_hash,
        "balance": balance,
        "transactions": []
    }

    save_accounts(accounts)

    print("\nAccount created successfully!")
    print("Account Holder Name:", name)
    print("Account Number:", account_no)
    print("Initial Balance:", balance)
