import pytest
from lib.password_checker import *

def test_password_checker_valid():
    password = PasswordChecker()
    assert password.check('12345678') == True

def test_password_checker_invalid():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('12345')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
