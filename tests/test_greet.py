from lib.greet import *

def test_greet_say_hello_name():
    result = greet("John")
    assert result == "Hello, John!"