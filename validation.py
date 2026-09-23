# we are making this file to validate the user input for account number, pin and amount

def valid_acc_no(account_number):
    return account_number.isdigit() and len(account_number) == 8

# isdigit() checks if the string consists of digits only and len() checks the length of the string. In this case, we are checking if the account number is 8 digits long and consists of digits only.
def valid_pin(pin):
    return pin.isdigit() and len(pin) == 4


def valid_amt(amount):
    return amount > 0