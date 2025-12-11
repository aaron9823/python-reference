print("hello "); print("world!")
"""
- semicolon in Python, semicolons are not required.
  In many other languages, each statement must end with a semicolon,
  but in Python, this is not optional and rarely used.
"""


if True:
    print("inside this block,")
    print("statements must be indented by 4 spaces")
print("outside the block, no indentation required")
"""
- code blocks(    ):
  Python uses indentation typically 4 spaces to define code blocks
  rather than braces '{}'.
"""


if True:            # if, while for all create their own code blocks
    a = 10          # these lines belong to the same block; indetation must match
    if a == 10:     
        print(a)
"""
indetation can be create using 2 spaces, 4 spaces, or tab.
but Python's style guide recommends 4 spaces per level.
"""


print("I don't want to say hello world")        # this comment will not be excuted.
"""
- comments :
  Python uses the '#' symbol for single-line comments.
  multi-line comments can be simulated using multi-line strings(''' or "" ")
"""