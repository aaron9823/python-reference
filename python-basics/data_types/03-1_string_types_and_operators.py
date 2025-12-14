s1 = "hello"
s2 = 'my name is'
s3 = '''Aaron'''
s4 = """This is my name."""
print(s1, type(s1), s2, type(s2), s3, type(s3), s4, type(s4))
"""
String Data Type

Python has a single string type: `str`.  
However, Python provides **four different ways to declare strings**:

    "double quotes"
    'single quotes'
    '''triple single quotes'''
    "" "triple double quotes"" "

These allow greater flexibility:

1) You can include single or double quotes inside a string without escaping:
       "it's fine"
       'he said "hi"'
   (Though escaping with \' or \" is also possible.)

2) Triple quotes allow multi-line strings without using newline characters (\n).

Strings are incredibly powerful in Python, with many built-in features and operations.
"""


s5 = '''
This is
a multi-line
string without needing \\n.
'''
print(s5)
"""
Multi-line strings can be used as actual string values,  
or as comment-like blocks when not assigned to a variable.

The reason this works is that an unused string literal is ignored
by the Python interpreter.
"""


s6 = "This looks like it's split, \
but it is actually one line."
s7 = "Hello""World"
print(s6, s7)
"""
You can join strings in two additional ways:

1) Use a backslash (\) to continue a line without adding whitespace.
2) Place two string literals next to each other.  
   Python automatically concatenates them.

Python also supports escape sequences (special characters)
similar to those in C.

Examples include:
    \\n  newline
    \\t  tab
    \\'  single quote
    \\"  double quote
    \\\\  backslash
"""


print(s1 + s2)
print(s3 * 5)
print(len(s4))
"""
String Operators:

Python provides unique behaviors for strings:

- +    concatenates strings
- *    repeats a string multiple times
- len  returns the length of the string

These can be used creatively, such as:
    print('-' * 20)
to easily create separators or repeated patterns in output.
"""

