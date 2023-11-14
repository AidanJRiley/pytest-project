from lib.new_grammar import *

def test_valid_text():
    assert grammar_check('Hello everyone.') == True

def test_no_capital_no_punctuation():
    assert grammar_check('hello everyone') == False

def test_capital_no_punctuation():
    assert grammar_check('Hello everyone') == False

def test_no_capital_punctuation():
    assert grammar_check('hello everyone.') == False

def test_question_mark():
    assert grammar_check('Hello everyone?') == True

def test_exclamation_mark():
    assert grammar_check('Hello eveyrone!') == True

def test_incorrect_punctuation():
    assert grammar_check('Hello everyone%') == False

def test_start_punctuation():
    assert grammar_check('%Hello everyone') == False