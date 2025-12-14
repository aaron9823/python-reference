"""
String Method Summary
"""

# -------------------------------------------------------------------
# 1. Case Conversion
# -------------------------------------------------------------------
"""
.upper()        → Converts all letters to uppercase.
.lower()        → Converts all letters to lowercase.
.swapcase()     → Swaps uppercase ↔ lowercase.
.capitalize()   → Capitalizes the first character of the string.
.title()        → Capitalizes the first letter of each word.
"""

# -------------------------------------------------------------------
# 2. Searching
# -------------------------------------------------------------------
"""
.count(x)       → Returns the number of occurrences of x.

# 2-1. find() and index()
.find(x)        → Returns the index of the first occurrence (left-most).  
.find(x, n)     → Starts searching from index n.  
.rfind(x)       → Returns the index of the last occurrence (right-most).

.index(x)       → Same as find(), but raises ValueError if x is not found.  
.index(x, n)    → Search starting from index n.  
.rindex(x)      → Right-side version of index().

Difference:
- find()  → returns -1 when not found  
- index() → raises an exception when not found
"""

# 2-2. startswith() & endswith()
"""
.startswith(x)          → True if the string starts with x.
.endswith(x)            → True if the string ends with x.

Both methods support:
    .startswith(x, start, end)
    .endswith(x, start, end)

Examples:
    s.endswith('on', 0, 5)
    s.startswith('A', 6)
"""

# -------------------------------------------------------------------
# 3. Replace & Strip
# -------------------------------------------------------------------
"""
.replace(x, y)     → Replaces all occurrences of x with y.
.expandtabs(n)     → Converts tabs (\t) into n spaces (default = 8).

.rstrip(x)         → Removes x from the right end (default: whitespace).
.lstrip(x)         → Removes x from the left end.
.strip(x)          → Removes x from both ends.
"""

# -------------------------------------------------------------------
# 4. Split & Join
# -------------------------------------------------------------------
"""
.split(x)          → Splits the string based on x.  
                      Default splitter = whitespace.

.split(x, n)       → Splits left-to-right, up to n times.
.rsplit(x, n)      → Splits right-to-left, up to n times.
.splitlines()      → Splits the string by newline characters.

'sep'.join(iterable)
                    → Inserts sep between all items in iterable.
"""

# -------------------------------------------------------------------
# 5. Alignment
# -------------------------------------------------------------------
"""
.center(n)         → Centers the string within width n.
.ljust(n)          → Left-aligns the string within width n.
.rjust(n)          → Right-aligns the string within width n.

All three accept a second argument to fill empty spaces:
    s.center(10, '*')
    s.ljust(10, '_')

.zfill(n)          → Right-aligns and pads with zeros.
"""

# -------------------------------------------------------------------
# 6. Character Type Checks (Return True or False)
# -------------------------------------------------------------------
"""
.isdigit()         → Contains only digits (0–9).
.isalpha()         → Contains only alphabetic characters.
.isalnum()         → Contains only alphanumeric characters.
.islower()         → All letters are lowercase.
.isupper()         → All letters are uppercase.
.isspace()         → Contains only whitespace.
.istitle()         → Each word starts with an uppercase letter.
"""

# -------------------------------------------------------------------
# 7. string Module
# -------------------------------------------------------------------
"""
The string module provides predefined character groups.

import string

string.digits        → "0123456789"
string.octdigits     → "01234567"
string.hexdigits     → "0123456789abcdefABCDEF"
string.ascii_letters → "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
string.ascii_lowercase
string.ascii_uppercase
string.punctuation   → !"#$%&'()*+,-./:;<=>?@[]^_`{|}~
string.printable     → All printable characters
string.whitespace    → All whitespace characters

Example:

import string

ch = "01234"
print(ch in string.digits)   # Returns True if character is a digit
"""
