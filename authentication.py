
import hashlib


def log(accounts):
    print("\n------Login------")

    lo_acc = input("Enter account number: ")
    lo_pin = input("Enter PIN: ")

    lo_pin_security = hashlib.sha256(lo_pin.encode()).hexdigest()

    if lo_acc in accounts and lo_pin_security == accounts[lo_acc]["pin"]:
        print("\nLogin successful!")
        print("Welcome,", accounts[lo_acc]["name"])

        return lo_acc

    print("\nInvalid account number or PIN. Please try again.")
    return None
