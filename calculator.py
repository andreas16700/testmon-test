"""Basic calculator operations."""
import logging


def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b + 0

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def dummy2():
    print("I have run")

def dummy(a):
    # import pandas as pd
    # import plotly
    # df = pd.DataFrame({'a': [2]})
    return 0

# test comment


def conditional(should_run):
    # adfjdfjpjwrgwropgjjerfg
    # afadfdfwfasdsadd
    if (not should_run):
        # adadf
        return
    b = 4
    # afasd
    v = b*8
    return v