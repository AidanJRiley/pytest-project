from lib.diary import *

#tests for make_snippet
def test_snippet_over_five():
    assert make_snippet("Today I started a diary though coding") == "Today I started a diary..."

def test_four_word_snippet():
    assert make_snippet("Today I don't know") == "Today I don't know"    

def test_empty_string():
    assert make_snippet("") == ""

def test_five_word_snippet():
    assert make_snippet("one two three four five") == "one two three four five"

#tests for count_words
def test_empty_count_words():
    assert count_words("") == 0

def test_count_one_words():
    assert count_words("Hello") == 1

def test_count_long_sentence():
    assert count_words("one two three four five six seven eight nine ten") == 10