from lib.make_snippet import make_snippet

# a function called 'make snippet' that takes a string
# as an argument and returns the first five words and 
# then a '...' if there are more than than that
"""
if given an empty string
it returns an empty string

"""
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""
"""
given a string of four words
It returns the same string 
"""
def test_given_four_string_returns_same_thing():
    result = make_snippet("one two three four")
    assert result == "one two three four"
"""
Givem a strong of five words
it returns the same string
"""
def test_given_five_string_returns_same_thing():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"
"""
Given a string of six words
It returns the first five words and a "..."
"""
def test_given_six_words_returns_string_and_ellipsis():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."
    

