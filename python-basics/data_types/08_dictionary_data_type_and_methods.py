from pprint import pprint
# pprint is a module that prints dictionaries in a more readable format.

dic1 = {1: 'one', 'two': 2, '3~5': [3, 4, 5]}
print(dic1)
"""
Dictionary:

A dictionary is a data type that stores data as key-value pairs.
It is similar to a real-world dictionary where words are mapped to meanings.

In computer science, this structure is also known as an associative array or hash map.

An empty dictionary can be created using {}.
The dict() function can be used to convert other data structures into a dictionary,
as long as the data consists of key-value pairs.

Examples:
    dict([[1, 'one'], [2, 'two']])
    dict((1, 'one'), (2, 'two'))

Each element in a dictionary has the form:
    key : value

- Keys must be immutable (e.g. int, str, tuple)
- Values can be mutable or immutable

Unlike lists or tuples, dictionaries do not use indexes.
Values are accessed using keys instead.

Dictionaries can be nested.
When iterating over a dictionary using:
    for key in dict:
only the keys are returned.
"""


dic2 = {1: 'one'}
print("initial:", dic2)

dic2[2] = ['two', '2']
print("after add:", dic2)

del dic2[1]
print("after delete:", dic2)

print("search by key:", dic2[2])

dic2[2] = '2'
print("after update:", dic2)
"""
Add, delete, search, and update in dictionaries:

Adding:
    dict[key] = value

Deleting:
    del dict[key]

Searching:
    dict[key]

Updating:
    dict[key] = new_value

Important:
Modifying a dictionary (adding or deleting keys) while iterating over it
will raise a runtime error.

Unlike dictionaries, lists allow size changes during iteration,
which can lead to unintended infinite loops.
"""


dic3 = {
    'AL EAST': ['NYY', 'TB', 'TOR'],
    'AL CENTRAL': ['MIL', 'PIT', 'STL'],
    'AL WEST': ['LAD', 'SD', 'SF']
}

print(dic3.keys(), list(dic3.keys()), sep="\nAs list: ")
"""
.keys():

Returns all keys in the dictionary.
In Python 3+, this returns a dict_keys view object instead of a list
to reduce memory usage.

The returned object is iterable and behaves like a list in most cases.
"""


print(dic3.values(), list(dic3.values()), sep="\nAs list: ")
"""
.values():

Returns all values in the dictionary.
Like .keys(), this returns a dict_values view object.
"""


print(dic3.items(), list(dic3.items()), sep="\nAs list: ")
"""
.items():

Returns all key-value pairs as tuples.
The return type is dict_items, which can be converted to a list if needed.
"""


print(dic3.get('AL EAST'), dic3.get('AL CENTRAL'), dic3.get('AL WEST'))
"""
.get():

Retrieves a value by key, similar to dict[key].

Difference:
- dict[key] raises KeyError if the key does not exist
- dict.get(key) returns None if the key does not exist

An optional second argument allows specifying a default return value
when the key is missing.
"""


print(dic3.fromkeys([1, 2, 3, 4]))
print(dic3.fromkeys((1, 2, 3, 4), 'value'))
print(dic3.fromkeys([1, 2, 3, 4], (10, 20, 30, 40)))
"""
.fromkeys():

Creates a new dictionary using the given iterable as keys.
All keys share the same value (default is None).

Important:
- This does NOT modify the original dictionary
- It returns a new dictionary

Similar to setdefault(), but applies to multiple keys at once.
"""


print("Pretty print output:")
pprint(dic3)
"""
Additional notes:

Using the 'in' operator with dictionaries checks for the existence of keys.
Example:
    'Taoism' in dic3   # True or False

The pprint() function prints dictionaries in a human-readable format,
displaying each key-value pair on a separate line.
"""

