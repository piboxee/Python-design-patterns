"""
Problem:
    New features to an existing object
    Dynamic changes
    Not using subclassing

Solution:
    Functions as object
    Built-in decorator feature
"""

from functools import wraps


def make_blink(function):
    """Defines the decorator"""
    @wraps(function)  # This makes the decorator transparent in terms of its name and docstrings
    def decorator():  # Define the inner function
        ret = function()  # Grab the return value of the function being decorated
        return "<blink>" + ret + "</blink>"  # Add new functionality to the function being decorated
    return decorator


@make_blink  # Apply the decorator here!
def hello_world():
    """Original function"""
    return "Hello, World!"


# Check the result of decorating
print(hello_world())

# Check if the function name is still the name of the function being decorated
print(hello_world.__name__)

# Check if the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)
