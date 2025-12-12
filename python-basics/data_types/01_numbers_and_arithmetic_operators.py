a = 1
b = 0
c = -9
print(a, type(a), b, type(b), c, type(c))
# type(variable) returns the data type of the given variable.
"""
Numeric Data Types

Numbers we typically use—integers, floating-point numbers, and complex numbers—
are collectively called numeric data types in Python.

Python provides three built-in numeric types:

- int      : integer numbers
- float    : floating-point (real) numbers
- complex  : complex numbers with real and imaginary parts
"""


d = -4.2
e = 4.2E1
print(d, type(d), e, type(e))

n1 = float('nan')
n2 = float('inf')
print(n1, type(n1), n2, type(n2))
"""
2) float (Floating-Point Numbers)

Floating-point numbers represent real numbers with decimal points.
Python supports up to roughly 15 significant digits.

The float() function converts values to floating-point numbers.

Special float values:
- inf  : positive infinity
- -inf : negative infinity
- nan  : not a number (undefined result)

Floating-point literals may also be written using scientific notation:
    4.2E1  → 42.0
"""


f = 0o12   # octal
g = 0x12   # hexadecimal
print(f, type(f), g, type(g))
"""
Octal, hexadecimal, and binary literals do NOT store special types internally.
Python automatically converts them to regular integers (base 10).
"""


h = 2 + 3j
print(h, type(h))
print(h.real, h.imag, h.conjugate(), abs(h))

i = 1j
print(i, i**2, i**3, i**4)
"""
3) complex (Complex Numbers)

Python supports complex numbers using the imaginary suffix j or J.

Examples:
    2 + 3j
    1j
    complex(3)       → 3 + 0j
    complex(3, 4)    → 3 + 4j
    complex('3+4j')  → 3 + 4j

Useful attributes and methods:
- .real        → real part
- .imag        → imaginary part
- .conjugate() → complex conjugate
- abs(x)       → magnitude (distance from origin)

Python also supports exponentiation of complex numbers.
"""


"""Numeric Operators:

Python supports the basic arithmetic operators:
    +   addition
    -   subtraction
    *   multiplication
    /   division

Additional numeric operators:
    **   exponentiation        (2**3 == 8)
    %    modulus (remainder)   (5%2 == 1)
    //   floor division        (5//2 == 2)
"""


