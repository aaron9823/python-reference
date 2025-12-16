formatting = "formatting"

print("operator %s" % formatting)              # Formatting style 1 (% operator)
print("str.format {f}".format(f=formatting))      # Formatting style 2 (str.format)
print(f"f-string {formatting}")   
"""
String Formatting:

String formatting refers to inserting values into a string.

In C, you can insert values into a string using format specifiers (e.g. %d, %s)
inside printf(). Python provides similar functionality for embedding values
into strings.

While simple string concatenation (+) works for small cases, formatting is
much more suitable for repetitive or complex string construction.

Python supports multiple formatting styles depending on the version:
- % operator     : legacy style (before Python 3.0)
- str.format()   : newer style (Python 3+)
- f-string       : modern style (Python 3.6+)

Note:
- With % formatting, use %% to output a literal percent sign.
- With {} formatting, use {{ and }} to output literal braces.
"""


test1 = "\n%s version" % "operator"
print(test1)

time = "%s %d. %d. %d." % ("Current day:", 2025, 12, 15)
print(time)

"""
% operator:

This is the oldest formatting style in Python and is similar to C's printf().
Format specifiers such as %s, %d, and %f are placed inside the string, and
values are provided after the string using the % operator.

Each format specifier must match the data type of the value.
If the types do not match, a runtime error occurs.

As the string grows longer, this style quickly becomes hard to read and
maintain.

Example:
    print(
        "I am %s, %d years old, live in %s, and my goal is to %s by %d."
        % (name, age, location, goal, year)
    )
"""


test2 = "\n{} version".format("str.format")
print(test2)

print("My name is {1} and I am {0}".format("27 years old", "Aaron"))
test3 = "Name: {name}, Age: {age}, From: {location}"
print(test3.format(name="Aaron", age="27", location="Toronto"))

dic = {"name": "No idea", "age": "20", "location": "LA"}
print(test3.format(**dic))
"""
str.format():

Introduced in Python 3.0 as a more flexible formatting approach.
The official documentation recommended this style before f-strings existed.

You define placeholders using {} and call the format() method on the string.

Values can be:
- Inserted by position (0, 1, 2, ...)
- Inserted by keyword
- Inserted using dictionary unpacking (**)

Although more readable than % formatting, long format() calls can still
reduce readability.
"""


new = "f-string"
print(f"\n{new} version")

zom = "kind of"
test4 = f"Please {zom} stop throwing {zom} strange errors while coding {zom}."
print(test4)

num = 1
print(f"This also works: {num}, {num + num}, {num + 2}")

li1 = ["I am", "Ohtani is"]
dic2 = {"Aaron": "27 years old.", "Ohtani": "31 years old"}
print(f"{li1[0]} {dic2['Aaron']} {li1[1]} {dic2['Ohtani']}")
"""
f-string:

Available in Python 3.6 and later.

You prefix the string with f and place variables or expressions directly
inside {}. No need to call format().

Any valid Python expression is allowed inside the braces, including:
- Arithmetic operations
- List indexing
- Dictionary lookups

Performance-wise, f-strings are generally faster than both % formatting
and str.format(), and they are also the most readable.

In modern Python codebases, f-strings are the recommended default.
"""