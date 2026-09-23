from storage import la
from account import create_acc
from authentication import log
from banking import _menu


accounts = la()


while True:
    print("\n=========== MINI BANKING SYSTEM ===========")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        create_acc(accounts)

    elif choice == "2":
        login_account = log(accounts)

        if login_account is not None:
            _menu(accounts, login_account)

    elif choice == "3":
        print("\nThank you for using the Mini Banking System")
        break

    else:
        print("\nInvalid Choice. Please try again.")