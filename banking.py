from storage import save_accounts
from validation import valid_amt


def banking_menu(accounts, login_account):
    current_acc = accounts[login_account]

    while True:
        print("\n--------Banking Menu--------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Account Details")
        print("7. Logout")

        banking_choice = input("Enter your choice: ")

        if banking_choice == "1":
            check_bal(current_acc)

        elif banking_choice == "2":
            depo_money(current_acc, accounts)

        elif banking_choice == "3":
            withdraw_money(current_acc, accounts)

        elif banking_choice == "4":
            transfer_money(accounts, login_account)

        elif banking_choice == "5":
            transaction_his(current_acc)

        elif banking_choice == "6":
            show_account_details(current_acc, login_account)

        elif banking_choice == "7":
            print("Logout Selected")
            save_accounts(accounts)
            break

        else:
            print("Invalid  choice. Please try again.")


def check_bal(account):
    print("\nYour current balance is:", account["balance"])


def depo_money(account, accounts):
    try:
        amount = float(input("Enter amount to deposit: "))

        if valid_amt(amount):
            account["balance"] += amount
            account["transactions"].append(
                "Deposited INR " + str(amount)
            )

            save_accounts(accounts)

            print(
                "Deposit successful! New balance:",
                account.get("balance")
            )
        else:
            print("Invalid amount. Please try again.")

    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def withdraw_money(account, accounts):
    try:
        amount = float(input("Enter amount to withdraw: "))

        if not valid_amt(amount):
            print("Invalid amount. Please try again.")

        elif amount > account.get("balance"):
            print("Insufficient balance. Please try again.")

        else:
            account["balance"] -= amount
            account["transactions"].append(
                "Withdrawn INR " + str(amount)
            )

            save_accounts(accounts)

            print(
                "Withdrawal successful! New balance:",
                account["balance"]
            )

    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def transfer_money(accounts, login_account):
    current_account = accounts[login_account]

    receiver_account = input("Enter receiver's account number: ")

    if receiver_account == login_account:
        print("You cannot transfer money to your own account. Please try again.")

    elif receiver_account not in accounts:
        print("Receiver account not found. Please try again.")

    else:
        try:
            amount = float(input("Enter amount to transfer: "))

            if not valid_amt(amount):
                print("Invalid amount. Please try again.")

            elif amount > current_account["balance"]:
                print("Insufficient balance. Please try again.")

            else:
                current_account["balance"] -= amount
                accounts[receiver_account]["balance"] += amount

                accounts[receiver_account]["transactions"].append(
                    "Received INR " + str(amount) + " from " + login_account
                )

                current_account["transactions"].append(
                    "Transferred INR " + str(amount) + " to " + receiver_account
                )

                save_accounts(accounts)

                print("Transfer successful!")
                print("Transferred amount:", amount)
                print(
                    "Remaining balance:",
                    current_account.get("balance")
                )

        except ValueError:
            print("Invalid amount.")


def transaction_his(account):
    print("\n---------Transaction History---------")

    if len(account["transactions"]) == 0:
        print("No transactions found.")

    else:
        for trans in account["transactions"]:
            print(trans)


def show_account_details(account, login_account):
    print("\n------Account Details------")
    print("Account Holder Name:", account[("name")])
    print("Account Number:", login_account)
    print("Current Balance:", account.get("balance"))
