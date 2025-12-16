nums = [1, 2, 3, 4, 5]

squared = [n ** 2 for n in nums]
print(squared)

evens = [n for n in nums if n % 2 == 0]
print(evens)

labels = ["even" if n % 2 == 0 else "odd" for n in nums]
print(labels)
"""
List Comprehension:
List comprehension is a concise syntax for creating a list
using a for-loop, optionally combined with conditions.

Basic syntax:
[expression for variable in iterable]

With condition:
[expression for variable in iterable if condition]

With conditional expression:
[value_if_true if condition else value_if_false for variable in iterable]

It replaces the common pattern of:
- creating an empty list
- looping
- appending values

List comprehensions are widely used in real-world Python code
because they are expressive and readable when kept simple.
"""


pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
"""
Nested List Comprehension:
A nested list comprehension contains more than one for-loop.

Syntax:
[expression for var1 in iterable1 for var2 in iterable2]

The execution order is the same as nested for-loops:
the leftmost for-loop runs first, then the next one.

Nested comprehensions are powerful but can reduce readability
if overused. In practice, they are usually limited to two levels.
"""


nums = [1, 2, 3, 4]

square_dict = {n: n ** 2 for n in nums}
print(square_dict)

filtered_dict = {n: n ** 2 for n in nums if n % 2 == 0}
print(filtered_dict)
"""
Dictionary Comprehension:
Dictionary comprehension is used to create dictionaries
in a compact and readable way.

Basic syntax:
{key_expression: value_expression for variable in iterable}

With condition:
{key_expression: value_expression for variable in iterable if condition}

It is commonly used for transforming or filtering key-value data.
"""


nums = [1, 2, 2, 3, 3, 4]

unique_squares = {n ** 2 for n in nums}
print(unique_squares)
"""
Set Comprehension:
Set comprehension creates a set using comprehension syntax.

Basic syntax:
{expression for variable in iterable}

Because sets do not allow duplicate values,
duplicates are automatically removed.

The syntax is similar to list comprehension,
but the result is a set instead of a list.
"""


gen = (n ** 2 for n in range(5))
print(gen)

tpl = tuple(gen)
print(tpl)
"""
Tuple and Comprehension:
There is no such thing as a "tuple comprehension" in Python.

Using parentheses () with comprehension syntax creates
a generator expression, not a tuple.

A generator produces values lazily (one at a time).
If a tuple is needed, the generator must be converted
using the tuple() function.
"""


bad_example = [x for x in range(10) if x % 2 == 0 if x > 3]
print(bad_example)
"""
Notes:
Comprehensions are best used when the logic is simple and clear.

If there are too many conditions or nested loops,
a normal for-loop may be more readable.

In real-world code:
- Use comprehensions for clarity and brevity
- Avoid them when they harm readability
"""

# List comprehension        -> []
# Dictionary comprehension -> {}
# Set comprehension         -> {}
# Tuple comprehension       -> Not supported (use generator)
