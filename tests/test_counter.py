from lib.counter import *

def test_counter_initally_reports_0():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_add_single_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

def test_counter_add_two_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    assert counter.report() == "Counted to 15 so far."