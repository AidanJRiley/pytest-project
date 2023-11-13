from lib.report_length import *

def test_length_sentence1():
    result = report_length("How long is a piece of string")
    assert result == "This string was 29 characters long."

def test_length_word():
    result = report_length("word")
    assert result == "This string was 4 characters long."

def test_length_alphabet():
    result = report_length("abcdefghijklmnopqrstuvwxyz")
    assert result == "This string was 26 characters long."