from string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words



def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("a") == "A"
    assert capitalize_words("") == ""
    assert capitalize_words("") == ""


def test_capitalize_words2():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("a") == "A"
    assert capitalize_words("") == ""
    assert capitalize_words("") == ""