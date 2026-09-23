import hashlib


def login(accounts):
    print("\n------Login------")

    login_acc = input("Enter account number: ")
    login_pin = input("Enter PIN: ")

    login_pin_security = hashlib.sha256(login_pin.encode()).hexdigest()

    if login_acc in accounts and login_pin_security == accounts[login_acc]["pin"]:
        print("\nLogin successful!")
        print("Welcome,", accounts[login_acc]["name"])

        return login_acc

    print("\nInvalid account number or PIN. Please try again.")
    return None
