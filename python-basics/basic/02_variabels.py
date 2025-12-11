x = 10
"""
- variable
  a varaible is a name that stores a value.
  you can create a variable and assign a value 
  using the format: 
    variable_name = value

- variable name rules
  1. you may use letters(A-Z, a-z), digits (0-9)
  2. variable names are case-sensitive.
  3. the first character must be a letter or an underscore(_).
  4. some special characters cannot be used(+, -, *, /, $, @, &, %, etc.).
  5. keywords/reserved words (if, for, while, and, or, etc.) cannot be used as variable names.

- = operator
  '=' operator is assignment operator.
  if you want checking equality, you can use '=='
  works in the form:
    left_value = right_value

  the right side is a value or expression, and the left side must be a variable name.
  if the variable already holds a value, the new assignment will overwrite it.

  Python values may be integers (int), floating-point numbers (float), strings (str),
  or many other types. See the Data Types section for more detail.
"""


a = 'hello world'
b = 1
print(a, b)

del a, b
"""
If you create variables, you may also delete them.
multiple variables can be deleted together as well.
"""


x, y, z = 1, 2, 3
print(x, y, z)

x = y = z = 1
print(x, y, z)

null = None
print(null)
"""
variables can be assigned in multiple ways:

- Tuple unpacking:
      x, y, z = 1, 2, 3

- Multiple variables receiving the same value:
      x = y = z = 1

for an empty or uninitialized variable, Python uses `None`
(the equivalent of `null` in many other languages).
"""


dollar = 150_000
print(dollar)
"""
when representing large numbers, Python allows underscores (_) as visual separators:

    150_000
    1_234_567_890

This is only for readability and does not affect the numeric value.

Do NOT use commas (,) because Python interprets that as a tuple.
(To format numbers with commas on output, use string formatting.)
"""


x = 100
y = 100
print(x, y)
print("Address of x:", id(x), "Address of y:", id(y))
"""
Important Concept: In Python, values are objects.**

A variable does not "contain" a value.  
Instead, it **references** an object in memory.
"""