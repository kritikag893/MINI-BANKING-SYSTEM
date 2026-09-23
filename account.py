
import hashlib

from storage import sa
from validation import valid_acc_no, valid_pin, valid_amt


def create_acc(accounts):
    print("\n-----Create Account-----")

    n = input("Enter account holder name: ")

    while True:
        acc_no = input("Enter 8-digit account number: ")

        if valid_acc_no(acc_no):
            if acc_no in accounts:


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
            bal= float(input("Enter initial balance: "))


            if valid_amt(bal):
                break
            else:
                print("Initial balance cannot be negative.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")



    accounts[acc_no] = {"name": n,"pin": pin_hash,"balance": bal,"transactions": []}

    sa(accounts)

    print("\nAccount created successfully!")
    print("Account Holder Name:", n)
    print("Account Number:", acc_no)
    print("Initial Balance:", bal)
