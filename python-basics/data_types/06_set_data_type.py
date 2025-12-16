s1 = {1, 2, 1}
s2 = {}
s3 = set([1, 2, 3])
s4 = set()
s5 = set("Hello")

print(s1, s2, s3, s4, s5)
print(type(s1), type(s2), type(s3), type(s4), type(s5))  # One of these is a spy: s2
"""
Set:

A set is an unordered collection of unique elements.
Duplicate values are automatically removed when a set is created.

Sets are written using {}.
However, using {} alone creates a dictionary, not a set.
To create an empty set, you must use set().

The set() function can also be used to convert other iterable objects
into a set.

Because sets are unordered, indexing and slicing are not supported.
"""


fs1 = frozenset([1, 2, 3])
fs2 = frozenset(s1)

print(fs1, type(fs1))
print(fs2, type(fs2))
"""
frozenset (immutable set):

A frozenset is an immutable version of a set.
It has the same properties as a set, but elements cannot be added,
removed, or modified.

frozenset objects are created using the frozenset() function.
Other than immutability, they behave the same as sets.
"""


s01 = {1, 2}
s02 = {2, 3}

print(s01 & s02)
print(s01 | s02)
print(s01 - s02)
print(s01 ^ s02)
"""
Set operations:

Sets support mathematical set operations:
- &  : intersection (common elements)
- |  : union (all elements)
- -  : difference (elements in the left set only)
- ^  : symmetric difference (elements not shared)

Logical operators such as and / or cannot be used for set operations.

Compound assignment operators are also supported:
&=, |=, -=, ^=

Subset operators:
- <=, >=  : subset / superset
- <, >    : proper subset / proper superset
"""


print(
    s01.intersection(s02),
    s01.union(s02),
    s01.difference(s02),
    s01.symmetric_difference(s02)
)
"""
Set methods:

Set operations can also be performed using methods:
- .intersection()          : intersection
- .union()                 : union
- .difference()            : difference
- .symmetric_difference()  : symmetric difference

Subset-related methods:
- .issubset()
- .issuperset()
"""


temp_s = {1, 2, 3}
temp_s.add(4)
print(temp_s)
"""
.add():
Adds a single element to the set.
"""


temp_s.update([5, 6, 7])
print(temp_s)
"""
.update():
Adds multiple elements to the set.
The argument must be an iterable.
"""


temp_s.remove(7)
temp_s.discard(6)
print(temp_s)
"""
.remove() and .discard():

Both remove an element from the set.

Difference:
- .remove()   : raises an error if the element does not exist
- .discard()  : does nothing if the element does not exist
"""


a = {1, 2, 3}
b = {1, 2}

print(a.issubset(b))
"""
.issubset():
Returns True if the given set is a subset of the target set.
"""


print(a.issuperset(b))
"""
.issuperset():
Returns True if the target set is a superset of the given set.

a.issubset(b) == b.issuperset(a)
"""


print(a.isdisjoint(b))
"""
.isdisjoint():
Returns True if the two sets have no elements in common.
"""