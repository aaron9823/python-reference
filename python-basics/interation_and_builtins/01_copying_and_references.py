import copy

"""
Simple Assignment vs Shallow Copy vs Deep Copy
"""


print("Simple assignment")

a = b = [1, 2, 3]
print(a, b)

del a[0]
print(a, b)
"""
Simple Assignment:
In Python, variables do not store values directly.
They store references to objects.

When using:
    a = b = [1, 2, 3]

Both 'a' and 'b' reference the same list object in memory.
Therefore, modifying the object through one variable
affects the other variable as well.

This behavior applies to mutable objects such as:
- list
- dict
- set

Immutable objects (int, float, bool, str, tuple) behave differently.
Any modification creates a new object instead of changing the original.
"""


print("\nShallow copy")

c = [1, 2, 3]
d = c.copy()

print(c, d)

del c[0]
print(c, d)


e = [1, [2, 3, 4]]
f = e.copy()

print(e, f)

del e[1][1]
print(e, f)
"""
Shallow Copy:
A shallow copy creates a new outer object,
but inner objects are still shared.

Methods that perform shallow copy:
- list.copy()
- dict.copy()
- copy.copy()

This means:
- The top-level container is duplicated
- Nested mutable objects remain referenced

As a result, modifying nested objects
affects both the original and the copied structure.
"""


print("\nDeep copy")

g = copy.deepcopy(e)
print(e, g)

del e[1][0]
print(e, g)
"""
Deep Copy:
A deep copy duplicates the entire object hierarchy recursively.

Using:
    copy.deepcopy()

- The outer object is copied
- All nested objects are copied as well
- No references are shared

This guarantees complete independence
between the original and the copied object.
"""


print("\nSelf-referencing example")

h = [1]
h.append(h)

print(h)
print(h.copy())
print(copy.deepcopy(h))
"""
Self-referencing objects:
An object can contain a reference to itself.

Shallow copy preserves the reference structure,
while deep copy safely recreates the structure
without causing infinite recursion.

This is one of the primary reasons deepcopy exists.
"""
