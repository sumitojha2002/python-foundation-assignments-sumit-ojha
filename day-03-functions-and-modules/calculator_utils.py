
# calculator_utils.py
# A small reusable module with basic math helper functions.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a,b):
    return a ** b

# A module-level constant, usable after import
VERSION = "1.0"


def power(base, exponent):
    return base ** exponent
