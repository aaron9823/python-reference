t1 = (1,)
t2 = (1, 2)
t3 = 1, 2, 3
t4 = ('a', 'b', ('ab', 'cd'))
t5 = tuple('hello')
t6 = tuple([1, 2, 3, 4])

print(t1, t2, t3, t4, t5, t6)
"""
Tuple:

A tuple is similar to a list, but unlike lists, tuples are immutable.
This means that elements cannot be modified, added, or removed after creation.

Because tuples are immutable, they are often faster than lists and can be
used safely for read-only data.

Tuples can be created in several ways:
- Using parentheses ()
- By separating values with commas (parentheses are optional)
- Using the tuple() function to convert an iterable into a tuple

Note:
A single-element tuple must include a trailing comma.
This is necessary to distinguish it from a non-sequence value.

Example:
    t01 = 1     # int
    t02 = 1,    # tuple
"""


def hello(seq):
    return seq[0], seq[-1]


print(hello("world!"))

first, last = hello("world!")
print(first, last)
"""
Useful facts about tuples:

When a function returns multiple values, Python automatically packs them
into a tuple.

The returned tuple can be unpacked into multiple variables.
This is similar to destructuring or unpacking assignment.

Nested unpacking is also supported:
    (a, (b, (c, d))) = (4, (3, (2, 1)))
"""


a = "K"
b = "R"

a, b = b, a
print(a, b)
"""
Variable swapping with tuples:

There is no need to use a temporary variable to swap values.
Tuple packing and unpacking allows swapping in a single line.
"""


tp = (1, 3, 5, 7, 9)
print(len(tp), max(tp), min(tp))
"""
Tuple built-in functions and methods:

Tuples support common built-in functions:
- len() : returns the number of elements
- max() : returns the largest element
- min() : returns the smallest element

Unlike lists, tuples have only two methods:
- .count()
- .index()
"""


print(tp.count(1), tp.index(1))
"""
.count() and .index():

- .count(x)  : returns the number of occurrences of x
- .index(x)  : returns the index of the first occurrence of x
These behave the same as their list counterparts.
"""
