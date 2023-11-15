from lib.diary_class import *

diary_title = "first day at makers"
ten = "one two three four five six seven eight nine ten "
diary_content_1 = "Today was my first day at makers. We had lots of meetings, and began learning to code."
diary_content_2 = "I didn't do much today."
three_hundred_word_count = ten * 30
five_hundred_word_count = ten * 50

def test_format():
    diary = DiaryEntry(diary_title,ten)
    assert diary.format() == "First Day At Makers: one two three four five six seven eight nine ten "

'''
#tests for make_snippet
def test_snippet_over_five():
    diary = DiaryEntry(diary_title,ten)
    assert make_snippet("Today I started a diary though coding") == "Today I started a diary..."

def test_four_word_snippet():
    assert make_snippet("Today I don't know") == "Today I don't know"    

def test_empty_string():
    assert make_snippet("") == ""

def test_five_word_snippet():
    assert make_snippet("one two three four five") == "one two three four five"
'''

#tests for count_words
def test_empty_count_words():
    diary = DiaryEntry("","")
    assert diary.count_words() == 1

def test_count_two_words():
    diary = DiaryEntry("one","two")
    assert diary.count_words() == 2

def test_count_long_sentence():
    diary = DiaryEntry(diary_title,ten)
    assert diary.count_words() == 14

def test_300_words_200_per_minute_reading_time():
    diary = DiaryEntry(diary_title,three_hundred_word_count)
    assert diary.reading_time(200) == 2

def test_10_words_200_per_minute_reading_time():
    diary = DiaryEntry(diary_title,ten)
    assert diary.reading_time(200) == 1

def test_1000_words_200_per_minute_reading_time():
    diary = DiaryEntry(diary_title,ten * 99)
    assert diary.reading_time(200) == 5

def test_reading_chunk_less_time():
    diary = DiaryEntry(diary_title,ten)
    assert diary.reading_chunk(200,2) == "First Day At Makers: one two three four five six seven eight nine ten"

def test_reading_chunk_1000_words_return_1():
    diary = DiaryEntry(diary_title,ten * 99)
    result = diary.reading_chunk(200,2)
    assert result == f"{diary_title.title()}: {ten*39}one two three four five six"

def test_reading_chunk_1000_words_return_2():
    diary = DiaryEntry(diary_title,ten*99)
    diary.reading_chunk(200,2)
    result = diary.reading_chunk(200,2)
    assert result == f"seven eight nine ten {ten*39}one two three four five six"

def test_reading_chunk_1000_words_return_3():
    diary = DiaryEntry(diary_title,ten*99)
    diary.reading_chunk(200,2)
    diary.reading_chunk(200,2)
    result = diary.reading_chunk(200,2)
    assert result == f"seven eight nine ten {ten*18}one two three four five six seven eight nine ten"
