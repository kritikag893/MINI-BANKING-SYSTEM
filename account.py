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
            pin_hash = hashlib.sha256(pin.encode()).hexdigest()
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
