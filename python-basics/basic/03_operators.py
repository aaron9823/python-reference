a = 10
b = 6
print(a + b, a - b, a * b, a / b, a ** b, a // b, a % b)
"""
Arithmetic Operators

Besides the basic operators (+, -, *, /), Python also provides:

- Exponentiation (**)
- Floor division (//)
- Modulus (%)

These allow you to perform power operations, integer division, and remainder calculations.
"""


a += 10
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a //= 10
print(a)
a %= 2
print(a)
"""
Assignment Operators

The basic assignment operator (=) assigns the right-hand value to the left-hand variable.

Compound assignment operators combine an arithmetic operation with assignment:

    a += 10   # a = a + 10
    a -= 10   # a = a - 10
    a *= 2    # a = a * 2
    a /= 2    # a = a / 2
    a **= 2   # a = a ** 2
    a //= 10  # a = a // 10
    a %= 2    # a = a % 2

They apply the arithmetic operation first and then assign the result back to the variable.
"""


print(a > b, a < b, a >= b, a <= b, a == b, a != b, a > b > 1)
"""
Comparison Operators

Comparison operators return True or False depending on the relationship
between two values:

    >, <, >=, <=, ==, !=

Python also supports **chained comparisons**, such as:

    a > b > 1

This evaluates both comparisons in a single expression.
"""


b1 = 0b1010  # binary 1010
b2 = 0b0101  # binary 0101
print(b1 & b2)
print(b1 ^ b2)
print(b1 | b2)
print(~b1)
print(b1 << 1)
print(b1 >> 1)
"""
Bitwise Operators

These operators perform boolean logic at the bit level:
vc
    &: AND
    |: OR
    ^: XOR
    ~: NOT (bitwise inversion)

Shift operators:
    <<: shift bits left
    >>: shift bits right
"""


bo1 = True
bo2 = False
print(bo1 and bo2)
print(bo1 or bo2)
print(not bo1)
"""
Logical Operators

Logical operators evaluate Boolean expressions:

    and
    or
    not
"""


hello = 1
print(hello in [1, 2, 3])
print(hello not in [1, 2, 3])
print([1, 2] in [1, 2, 3])
"""
Membership Operators

The membership operators check whether a value exists within a collection:

    value in sequence
    value not in sequence

They return True or False based on whether the element is present.
"""


n1 = 256
n2 = 256
print(id(n1), id(n2))
print(n1 is n2)
print(n1 is not n2)
"""
Identity Operators

`is` and `is not` check whether two variables refer to the **same object** in memory,
not whether their values are equal.

    a == b   → compares values
    a is b   → compares identity (memory reference)
"""


t1 = 4
t2 = 5
print("Even" if t1 % 2 == 0 else "Odd")
print("Even" if t2 % 2 == 0 else "Odd")
"""
Ternary Operator (Conditional Expression)

Python provides a concise form of conditional selection:

    value_if_true if condition else value_if_false

This is similar to if–else, but it returns a value instead of executing a block.
"""



