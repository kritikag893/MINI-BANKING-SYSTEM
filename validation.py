
def valid_acc_no(account_number):
    return account_number.isdigit() and len(account_number) == 8


def valid_pin(pin):
    return pin.isdigit() and len(pin) == 4




def valid_amt(amount):
    return amount > 0