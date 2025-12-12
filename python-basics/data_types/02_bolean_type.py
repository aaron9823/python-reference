b1 = True
b2 = False
print(b1, type(b1), b2, type(b2))
"""
Boolean Data Type

A boolean value in Python is represented by the `bool` type.
It holds one of two logical values:

    True   (1)
    False  (0)

Booleans are commonly used in conditional statements such as if and while.

Even without explicitly using bool values, Python evaluates many objects
as either truthy or falsy:

Falsy values include:
    [], (), {}, 0, "", None

Truthy values include:
    Any non-empty sequence/collection, any non-zero number,
    and any value that is not falsy.

The bool() function returns True or False based on how a value is interpreted
in a boolean context.

Comparison operators and logical operators also return boolean values.
(Those operators are explained in a separate section.)
"""


print(bool([]), bool({}), bool(0), bool(""), bool(None))
print(bool([1]), bool({1}), bool(-3), bool("wow"), bool(0.1))

print(not None)
"""
Empty containers, zero, empty strings, and None are evaluated as False.

Non-empty containers, non-zero numbers, and non-empty strings
are evaluated as True.

The `not` operator negates a boolean value.
"""
