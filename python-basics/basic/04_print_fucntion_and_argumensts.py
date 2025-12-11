import sys

print("What""Difference")
print("What", "difference")
print("What" + "difference")
"""
print() Function

Similar to C's printf(), Python uses the print() function to output values.

When two strings are placed side by side inside the same pair of quotes,
or when they are concatenated with +,
they are printed without any spaces.

However, using commas (,) in print() will insert a space between elements
because commas separate arguments, not string content.
"""


num = 1
chars = "One is"
print(chars, num)
# print(chars + num)      # This causes an error!
print(chars + str(num))   # Convert types to match before using +
"""
When combining multiple values inside print(), commas are allowed because
print() accepts multiple arguments.

But + only works when both sides are strings.
If they are not, you must convert types manually.
"""


print("Ba", "na", "na")
print("Ba", "na", "na", sep='')
print("Ba", "na", "na", sep=".", end='\n')
print("Ba", "na", "na", file=sys.stdout, flush=False)
"""
print() parameters:

sep=
    Specifies the separator inserted between each argument.
    Default: a single space ' '

end=
    Specifies what is printed after the last value.
    Default: newline character '\n'

file=
    Specifies the output stream.
    Default: sys.stdout (standard output, usually the screen)

flush=
    If True, forces the stream to flush its buffer immediately.
    Default: False
"""
