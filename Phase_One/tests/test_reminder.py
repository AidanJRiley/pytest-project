import pytest
from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

#This doesn't work for checking error messages
'''
def test_reminder():
    reminder = Reminder("Kay")
    result = reminder.remind()
    assert result == "No reminder set!"'''

#This is the format to use to get pytest to check error messages
def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"