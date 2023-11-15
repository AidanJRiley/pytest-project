from lib.grammar_class import *

def test_valid_sentence_full_stop():
    grammar = GrammarStats()
    result = grammar.check_grammar("A long time ago.")
    assert result == True

def test_valid_sentence_exclamation_mark():
    grammar = GrammarStats()
    result = grammar.check_grammar("Both of them!")
    assert result == True

def test_valid_sentence_question_mark():
    grammar = GrammarStats()
    result = grammar.check_grammar("Can't you see?")
    assert result == True

def test_invalid_sentence_asteriks():
    grammar = GrammarStats()
    result = grammar.check_grammar("Doesn't it seem brilliant*")
    assert result == False

def test_invalid_sentence_slash():
    grammar = GrammarStats()
    result = grammar.check_grammar("Every single time/")
    assert result == False

def test_multiple_sentence_valid():
    grammar = GrammarStats()
    result = grammar.check_grammar("Haven't you heard? They're on the move.")
    assert result == True

def test_multiple_sentence_invalid():
    grammar = GrammarStats()
    result = grammar.check_grammar("i don't know. What do you think?")
    assert result == False

def test_invalid_sentence_lower_case_one():
    grammar = GrammarStats()
    result = grammar.check_grammar("for goodness sake!")
    assert result == False

def test_invalid_sentence_lower_case_two():
    grammar = GrammarStats()
    result = grammar.check_grammar("go ahead, get trampled by a rhino&")
    assert result == False

def test_percentage_good_all_correct():
    grammar = GrammarStats()
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello.")
    assert grammar.percentage_good() == 100

def test_percentage_good_2_input_1_wrong():
    grammar = GrammarStats()
    grammar.check_grammar("Hello.")
    grammar.check_grammar("hello")
    assert grammar.percentage_good() == 50

def test_percentage_good_10_input_7_correct():
    grammar = GrammarStats()
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello.")
    grammar.check_grammar("Hello./")
    grammar.check_grammar("Hello./")
    grammar.check_grammar("Hello./")
    assert grammar.percentage_good() == 70