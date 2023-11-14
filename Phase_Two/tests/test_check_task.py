import pytest
from lib.check_task import *

def test_text_begins_with_TODO():
    text = '#TODO: Bake a cake'
    assert check_task(text) == True

def test_text_ends_with_TODO():
    text = 'Read a book #TODO'
    assert check_task(text) == True

def test_text_TODO_middle():
    text = 'Do exercise #TODO class'
    assert check_task(text) == True

def test_text_not_include_TODO():
    text = 'Eat chocolate'
    assert check_task(text) == False

def test_text_include_TODO_no_hash():
    text = 'TODO: practise Python'
    assert check_task(text) == False

def test_blank_text():
    text = ""
    with pytest.raises(Exception) as e:
        check_task(text)
    error_message = str(e.value)
    assert error_message == "Please insert valid text"

def test_text_is_int():
    text = 12345
    with pytest.raises(Exception) as e:
        check_task(text)
    error_message = str(e.value)
    assert error_message == "Please insert valid text"

