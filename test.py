from validation import valid_acc_no, valid_pin, valid_amt
def test_accno():
    assert valid_acc_no("12345678") == True
    assert valid_acc_no("123456789") == False
    assert valid_acc_no("12345678901") == False
    assert valid_acc_no("abcdefghij") == False
    assert valid_acc_no("12345abcde") == False
    print("Account number validation passed.")

def test_amt():
    assert valid_amt(100.0) == True
    assert valid_amt(-50.0) == False
    assert valid_amt(0.0) == False
    print("Amount validation passed.")

def test_pin():
    assert valid_pin("1234") == True
    assert valid_pin("abcd") == False
    assert valid_pin("12") == False
    assert valid_pin("12345") == False
    print("pin validation passed.")

test_accno()
test_amt()
test_pin()

print("\nAll tests passed successfully.")