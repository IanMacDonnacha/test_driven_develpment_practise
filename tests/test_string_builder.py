from lib.string_builder import *

def test_string_builder_size():
    string_builder = StringBuilder()
    string_builder.add("House")
    result = string_builder.size()
    assert result == 5

def test_string_builder_output():
    string_builder = StringBuilder()
    string_builder.add("House")
    result = string_builder.output()
    assert result == "House"

def test_string_builder_size_2():
    string_builder = StringBuilder()
    string_builder.add("House")
    string_builder.add("House")
    result = string_builder.size()
    assert result == 10

def test_string_builder_output_2():
    string_builder = StringBuilder()
    string_builder.add("House")
    string_builder.add("House")
    result = string_builder.output()
    assert result == "HouseHouse"