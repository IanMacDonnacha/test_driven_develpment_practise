from lib.report_length import *

def test_report_length_string_house():
    result = report_length("house")
    assert result == "This string was 5 characters long"

def test_report_length_string_integers():
    result = report_length("55997601")
    assert result == "This string was 8 characters long"

def test_report_length_string_special_char():
    result = report_length("!$%^&%£$£")
    assert result == "This string was 9 characters long"