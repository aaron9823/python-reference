a = [1, 2, 3]
print(a)

a.append(4)
a.append([1, 2])
print(a)
"""
.append():

Adds a single element to the end of the list.

The argument can be:
- a single value
- another list
- any object

When a list is passed, it is added as a single element,
not merged into the original list.

Note:
A list can even append itself, which creates a recursive structure.
'''
# loop = ['infinite']
# loop.append(loop)
# print(loop, loop[1], loop[1][1][1][1])
"""

b = [2, 3, 1]
b2 = ['d', 'c']

b.sort()
b2.sort()

print(b, b2)
"""
.sort():

Sorts the elements of the list in ascending order.

- Numbers are sorted numerically
- Strings are sorted lexicographically (ASCII / Unicode order)

Lists containing mixed data types cannot be sorted.

Note:
- .sort() modifies the original list
- sorted(list) returns a new sorted list

Use reverse=True to sort in descending order.
"""


c = ['Here', 'we', 'are', 'do not', 'turn', 'away', 'now']

for ch in c:
    print(ch, end=' ')
print()

c.reverse()

for ch in c:
    print(ch, end=' ')
print()
"""
.reverse():

Reverses the order of elements in the list.

This is NOT the same as sorting in reverse order.
To sort in descending order, use:
    list.sort(reverse=True)

Note:
- reversed(list) is a built-in function that returns an iterator
"""

d = [1, 2, 3]

print("popped value:", d.pop())
print(d)

d.extend([3, 4])
print(d)
"""
Other List Methods:

.count(x)   : returns the number of occurrences of x
.copy()     : returns a shallow copy of the list
.clear()    : removes all elements from the list
"""