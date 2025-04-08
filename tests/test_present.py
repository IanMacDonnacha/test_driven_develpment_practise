import pytest
from lib.present import *

def test_present_wrap():
    present = Present()
    present.wrap(55)
    assert present.unwrap() == 55

def test_present_wrap_err_msg():
    present = Present()
    with pytest.raises(Exception) as err:
        present.wrap()
        err_msg = str(err.value)
        assert err_msg == "A contents has already been wrapped."

def test_present_unwrap_err_msg():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
        err_msg = str(err.value)
        assert err_msg == "No contents have been wrapped."