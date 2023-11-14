from lib.check_grammar import *

def test_valid_sentence_full_stop():
    result = check_grammar("A long time ago.")
    assert result == True

def test_valid_sentence_exclamation_mark():
    result = check_grammar("Both of them!")
    assert result == True

def test_valid_sentence_question_mark():
    result = check_grammar("Can't you see?")
    assert result == True

def test_invalid_sentence_asteriks():
    result = check_grammar("Doesn't it seem brilliant*")
    assert result == False

def test_invalid_sentence_slash():
    result = check_grammar("Every single time/")
    assert result == False

def test_multiple_sentence_valid():
    result = check_grammar("Haven't you heard? They're on the move.")
    assert result == True

def test_multiple_sentence_invalid():
    result = check_grammar("i don't know. What do you think?")
    assert result == False

def test_invalid_sentence_lower_case_one():
    result = check_grammar("for goodness sake!")
    assert result == False

def test_invalid_sentence_lower_case_two():
    result = check_grammar("go ahead, get trampled by a rhino&")
    assert result == False