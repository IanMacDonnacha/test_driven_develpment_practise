import pytest
from lib.password_checker import *

def test_check_password_length_letters():
    check_password = PasswordChecker()
    result = check_password.check("horsehouse")
    assert result == True

def test_check_password_length_integers():
    check_password = PasswordChecker()
    result = check_password.check("123456789")
    assert result == True

def test_check_password_length_special_characted():
    check_password = PasswordChecker()
    result = check_password.check("!£$%^&*$")
    assert result == True

def test_check_password_length_mixed():
    check_password = PasswordChecker()
    result = check_password.check("horse123!")
    assert result == True

def test_check_password_length_error_lengh_less_than_8():
    check_password = PasswordChecker()
    with pytest.raises(Exception) as err:
        check_password.check("hors")
    err_msg = str(err.value)
    assert err_msg == "Invalid password, must be 8+ characters."