# no_char = "my name is Aaron"
# print(no_char[2], no_char[-4])

# """
# Indexing & Slicing

# Indexing retrieves a single character from a string using the syntax:
#     variable_name[n]

# The index starts at 0 and goes up to (length - 1).  
# If `n` is negative, Python starts counting from the end of the string:
#     -1 → last character
#     -2 → second-to-last
# and so on.
# """


# print(no_char[:], no_char[3:], no_char[3:7], no_char[4:7:2], no_char[6:3:-2])

# """
# Slicing extracts multiple characters using the syntax:
#     variable_name[start:end:step]

# Patterns:
# - s[:]          → entire string  
# - s[n:]         → from index n to the end  
# - s[:m]         → from start to index m-1  
# - s[n:m]        → from index n to m-1  
# - s[n:m:k]      → from n to m-1, stepping by k  

# Note:
# Python slicing follows the rule:
#     start <= index < end

# `start`, `end`, and `step` can all be negative.  
# A negative `step` iterates backward.
# """


str = "can i get your name? my name is Aaron."

print(str.count('.'))
# Returns how many times the given substring appears.

print(str.find('e'))
# Returns the index of the first occurrence. Returns -1 if not found.

print(str.index('e'))
# Same as find(), but raises a ValueError if not found.

print('-'.join(str))
# Inserts the given separator between each character or list element.

print(str.upper())
# Converts all alphabetic characters to uppercase.

print(str.lower())
# Converts all alphabetic characters to lowercase.

print(str.replace('Aaron', 'Hyunsu'))
# Replaces all occurrences of the first argument with the second argument.

print(str.split(' '))
# Splits the string into a list based on the given delimiter
# (default: whitespace).

str2 = "       I need some space       "
print(str2.lstrip(), "<end of string")
# Removes leading whitespace.

print(str2.rstrip(), "<end of string")
# Removes trailing whitespace.

print(str2.strip(), "<end of string")
# Removes whitespace on both sides.
"""
String Methods

Strings provide many built-in methods accessible through dot notation.
Below are some commonly used ones.  
(See section 03-3 for more detailed explanations.)
"""