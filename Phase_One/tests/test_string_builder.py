from lib.string_builder import *

def test_string_builder_initialise_blank():
    string = StringBuilder()
    assert string.output() == ""

def test_string_builder_add_word():
    string = StringBuilder()
    string.add("word")
    assert string.output() == "word"

def test_string_builder_add_multiple_words():
    string = StringBuilder()
    string.add("Hello ")
    string.add("World")
    assert string.output() == "Hello World"

def test_string_builder_length_initialise():
    string = StringBuilder()
    assert string.size() == 0

def test_string_builder_length_add_word():
    string = StringBuilder()
    string.add("word")
    assert string.size() == 4

def test_string_builder_length_add_multiple_words():
    string = StringBuilder()
    string.add("Hello ")
    string.add("World")
    assert string.size() == 11