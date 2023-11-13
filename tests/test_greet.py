from lib.greet import *

def test_greet_returns_for_Ann():
    result = greet("Ann")
    assert result == "Hello, Ann!"