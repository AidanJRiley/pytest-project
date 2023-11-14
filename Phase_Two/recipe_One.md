# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text):
    """
    Parameters: (list all parameters and their types)
      text: a string containing words

    Returns: (state the return value and its type)
        an int giving the estimated reading time based on an assumption of reading 200 words per minute

    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text of 200 words
It returns a time of 1 minute
"""
estimate_reading_time(text of 200 words) => [1 minute]

"""
Given a text of 100 words
It returns a time of 30 seconds
"""
estimate_reading_time(text of 100 words) => [30 seconds]

"""
Given an empty text
It returns a time of 0 minutes
"""
estimate_reading_time("") => [0 minutes]

"""
Given a text of 300 words
It returns a time of 1 minute 30 seconds
"""
estimate_reading_time(text of 300 words) => [1 minute 30 seconds]

'''
Given a text of 500 words
It returns a time of 2 minutes 30 seconds
'''
estimate_reading_time(text of 500 words) => [2 minutes 30 seconds]

'''
Given a text of 400 words
It returns a time of 2 minutes
'''
estimate_reading_time(text of 400 words) => [2 minutes]

'''
Given a text of 3 words
It returns a time of 1 second
'''
estimate_reading_time(text of 3 words) => [1 second]

'''
Given a text of 203 words
It returns a time of 1 minute 1 second
'''
estimate_reading_time(text of 203 words) => [1 minute 1 second]

'''
Given a text of 403 words
It returns a time of 2 minutes 1 second
'''
estimate_reading_time(text of 403 words) => [2 minutes 1 second]

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
