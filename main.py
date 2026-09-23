from storage import load_accounts
from account import create_acc
from authentication import login
from banking import banking_menu


accounts = load_accounts()


while True:
    print("\n=========== MINI BANKING SYSTEM ===========")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_acc(accounts)

    elif choice == "2":
        login_account = login(accounts)

        if login_account is not None:
            banking_menu(accounts, login_account)

    elif choice == "3":
        print("\nThank you for using the Mini Banking System")
        break

    else:
        print("Invalid Choice. Please try again.")