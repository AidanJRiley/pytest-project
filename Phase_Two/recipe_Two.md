# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammar(sentence):
    """
    Parameters: (list all parameters and their types)
      sentence: a string containing words

    Returns: (state the return value and its type)
        a boolean confirming whether the sentence starts with a capital letter and ends with a suitable sentence-ending punctuation mark

    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
['.','!','?']

"""
Given a sentence starting with a capital A and ending with a full stop
It returns True
"""
check_grammar("A long time ago.") => [True]

"""
Given a sentence starting with a capital B and ending with an exclamation mark
It returns True
"""
check_grammar("Both of them!") => [True]

"""
Given a sentence starting with a Capital C and ending with a question mark
It returns True
"""
check_grammar("Can't you see?") => [True]

"""
Given a sentence starting with a capital D and ending with a *
It returns False
"""
check_grammar("Doesn't it seem brilliant*") => [False]

'''
Given a sentence starting with a capital E and ending with a /
It returns False
'''
check_grammar("Every single time/") => [False]

'''
Given a text with multiple sentences in it with the first sentence beginning with a capital letter and the last sentence ending with valid punctuation
It only checks the beginning of the first sentence, and the end of the last sentence
'''
check_grammar("Haven't you heard? They're on the move.") => [True]

'''Given a text with multiple sentences in it where the first sentence does not begin with a capital letter but the last sentence ends with valid punctiation
It returns False
'''
check_grammar("i don't know. What do you think?") => [False]

'''
Given a text starting with a lower case F and ending with a .
It returns False
'''
check_grammar("for goodness sake!") => [False]

'''
Given a text starting with a lower case G and ending with a &
It returns False
'''
check_grammar("go ahead, get trampled by a rhino&") => [False]


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
