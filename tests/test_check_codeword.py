from lib.check_codeword import *

def test_check_codeword_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_for_letters_h_and_e():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_codeword_for_incorrect_codeword():
    result = check_codeword("kitten")
    assert result == "WRONG!"