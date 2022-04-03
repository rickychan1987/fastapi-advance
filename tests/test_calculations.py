from app.calculations import add, subtract, multiply, divide, BankAccount


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(3, 7) == 21


def test_divide():
    assert divide(30, 5) == 6


def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50
