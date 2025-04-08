from lib.counter import *

def test_counter_to_count_5():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counter to 5 so far."

def test_counter_to_count_999():
    count = Counter()
    count.add(999)
    result = count.report()
    assert result == "Counter to 999 so far."