from lib.gratitudes import *

def test_gratitudes_initialise_empty():
    grat = Gratitudes()
    assert grat.gratitudes == []

def test_gratitudes_add_one():
    grat = Gratitudes()
    grat.add("chocolate")
    assert grat.gratitudes == ['chocolate']

def test_gratitudes_add_two():
    grat = Gratitudes()
    grat.add("chocolate")
    grat.add("coding")
    assert grat.gratitudes == ['chocolate', 'coding']

def test_gratitudes_initialise_format():
    grat = Gratitudes()
    assert grat.format() == "Be grateful for: "

def test_gratitudes_add_one_format():
    grat = Gratitudes()
    grat.add("chocolate")
    assert grat.format() == "Be grateful for: chocolate"

def test_gratitudes_add_two_format():
    grat = Gratitudes()
    grat.add("chocolate")
    grat.add("coding")
    assert grat.format() == "Be grateful for: chocolate, coding"