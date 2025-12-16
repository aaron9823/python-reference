print("{0:ㅡ^+10,}".format(9999.9))

"""
Format Specifiers:

When inserting values into a string (string formatting), you can control
how the value is displayed using format specifiers.

In the old % formatting style, format specifiers are placed after %.
In modern formatting styles using {}, you can specify them as:

    {value:format_spec}

The full structure of a format specifier looks like this:

    <fill><align><sign><width><grouping><precision><type>
"""


print(
    "Default alignment : [{0:10}]\n"
    "Left aligned      : [{0:<10}]\n"
    "Center aligned    : [{0:^10}]\n"
    "Right aligned     : [{0:>10}]"
    .format("Hello")
)

print(
    "Default alignment : [{0:10}]\n"
    "Left aligned      : [{0:<10}]\n"
    "Center aligned    : [{0:^10}]\n"
    "Right aligned     : [{0:>10}]"
    .format(1234)
)

print(
    "Fill (number)     : [{0:0^10}]\n"
    "Fill (character) : [{0:A^10}]\n"
    "Fill (symbol)    : [{0:_^10}]\n"
    "Fill (symbol)    : [{0:□^10}]"
    .format(2020)
)
"""
Alignment, Width, and Fill Characters:

Alignment options:
- <  : left alignment
- ^  : center alignment
- >  : right alignment

Default alignment:
- Strings → left-aligned
- Numbers → right-aligned

The width value (e.g. 10) specifies the total output width.
If the value is shorter than the width, padding is added.

Fill characters can be specified before the alignment symbol.
If omitted, spaces are used by default.
"""


print(
    "Default sign      : {0:}, {1:}\n"
    "Always show sign : {0:+}, {1:+}\n"
    "Negative only    : {0:-}, {1:-}\n"
    "Sign at front    : {0:=+5}, {1:=5}"
    .format(3, -3)
)
"""
Sign Options:

Sign handling options:
- +  : always show the sign
- -  : show sign only for negative numbers (default)
- =  : place the sign at the far left, before padding

To fix the sign at the front and show all signs,
use the order: =+

Note:
Sign options are only valid for numeric types.
Using them with strings raises an error.
"""


print(
    "Default      : {0:}\n"
    "Comma        : {0:,}\n"
    "Underscore   : {0:_}"
    .format(2500000)
)
"""
Grouping Options:

Grouping options insert separators for large numbers:
- ,  : comma as thousands separator
- _  : underscore as thousands separator

Useful for displaying currency or large numeric values clearly.
"""


print(
    "Default (10 digits) : {0:}\n"
    "Up to 5 digits     : {0:.5}\n"
    "Up to 1 digit      : {0:.1}\n"
    "Up to 20 digits    : {0:.20}"
    .format(3.1415926535)
)
"""
Precision:

Precision is specified as:
    .<number>

For floating-point numbers, this limits the number of significant digits.
If the specified precision exceeds the actual precision of the float,
extra digits may appear due to floating-point representation errors.
"""


print(
    "Default        : {0:}\n"
    "Binary         : {0:b}\n"
    "Decimal        : {0:d}\n"
    "Hex (lower)    : {0:x}\n"
    "Hex (upper)    : {0:X}"
    .format(63)
)
"""
Type Specifiers:

Common type specifiers include:
- s  : string
- b  : binary
- d  : decimal integer
- o  : octal
- x  : hexadecimal (lowercase)
- X  : hexadecimal (uppercase)
- f  : fixed-point number
- e/E, g/G, n : various numeric formats

Type specifiers allow numbers to be displayed in different bases
or numeric representations.
"""