lst = [1, 2, 3, 4, 5]
tpl = (10, 20, 30)
s = "python"
r = range(5)

print(3 in lst)
print(100 not in tpl)

print(lst + [6, 7])
print(s * 2)

print(len(lst))
print(max(lst))
print(min(lst))
"""
Sequence types (list, tuple, string, range) support a common set of operations.

Membership operators:
- value in sequence       : checks if the value exists in the sequence
- value not in sequence   : checks if the value does not exist in the sequence

Concatenation and repetition:
- sequence + sequence     : creates a new sequence by combining two sequences
- sequence * integer     : repeats the sequence a given number of times

Built-in functions:
- len(sequence)           : returns the number of elements
- max(sequence)           : returns the largest element
- min(sequence)           : returns the smallest element
"""


lst = [10, 20, 30, 40, 50]

print(lst[0])
print(lst[-1])

lst[1] = 99
print(lst)

del lst[2]
print(lst)
"""
Indexing:

- sequence[index]         : accesses an element by index
- indexing starts at 0
- negative indexes access elements from the end (-1 is the last element)

Lists are mutable:
- elements can be modified or deleted using indexing

Note:
- strings and tuples support indexing
- but they are immutable and cannot be modified
"""


nums = [0, 1, 2, 3, 4, 5, 6]

print(nums[2:5])
print(nums[:4])
print(nums[3:])
print(nums[:])

print(nums[::2])
print(nums[::-1])
"""
Slicing:

- sequence[start:end]         : extracts elements from start to end-1
- sequence[start:end:step]    : extracts elements with a step value

Common slicing patterns:
- [:]       : entire sequence
- [::2]     : every second element
- [::-1]    : reversed sequence

Slicing always creates a new sequence.
"""


nums = [1, 2, 3, 4, 5, 6]

nums[1:4] = [10, 20, 30]
print(nums)

nums[::2] = [100, 200, 300]
print(nums)

del nums[2:4]
print(nums)
"""
Slice assignment and deletion:

- slice assignment replaces multiple elements at once
- step-based slice assignment must match the number of assigned elements

These operations are only possible on mutable sequence types (list).
Strings and tuples do not support slice assignment or deletion.
"""