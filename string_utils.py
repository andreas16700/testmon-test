"""String utility functions."""

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def is_palindrome(s):
    """Check if a string is a palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == reverse_string(cleaned)

def count_vowels(s):
    """Count vowels in a string."""
    vowels = "aeiouyYAEIOU"
    return sum(1 for char in s if char in vowels)

def capitalize_words(s):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in s.split())
