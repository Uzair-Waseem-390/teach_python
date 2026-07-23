# Errors and Their Types

# When writing programs, mistakes are NORMAL - even experienced developers
# make them every day. What matters is understanding WHAT KIND of mistake
# you're dealing with, since that tells you HOW to fix it.
# An "error" is anything that prevents your program from running correctly.


# 1. Syntax Errors
"""
A syntax error happens when your code breaks the GRAMMAR RULES of the
programming language. The interpreter can't even understand what you meant,
so the program won't run AT ALL - not even one line.

Example (invalid Python syntax):
    print("Hello"          # missing closing parenthesis
    if True                 # missing colon :
        print("Hi")

This is like writing a sentence with broken grammar in English - the reader
gets confused before even understanding the intended meaning.

Syntax errors are usually the EASIEST to fix, since Python tells you exactly
which line the problem is on.
"""


# 2. Runtime Errors (Exceptions)
"""
A runtime error happens WHILE the program is running - the syntax is
perfectly valid, but something goes wrong during execution that Python
can't recover from on its own.

Examples:
    print(10 / 0)              # ZeroDivisionError - dividing by zero
    print(my_list[100])         # IndexError - index doesn't exist
    print(undefined_variable)    # NameError - variable was never created
    num = int("hello")            # ValueError - "hello" can't become an int

These are also called EXCEPTIONS in Python. Later (in the Exception Handling
phase) you'll learn to catch and handle these gracefully using try/except,
instead of letting the whole program crash.
"""


# 3. Logical Errors
"""
A logical error is the trickiest kind - the code runs WITHOUT crashing,
and looks fine, but produces the WRONG result because the LOGIC itself
is flawed.

Example:
    # Trying to calculate the average of two numbers, but there's a bug
    num1 = 10
    num2 = 20
    average = num1 + num2 / 2   # BUG: this calculates num1 + (num2/2), not
                                  # (num1+num2)/2, due to operator precedence
    print(average)               # prints 20.0 instead of the correct 15.0

No error message is shown for a logical error - the program runs "successfully"
but gives you the wrong answer. These are found through careful testing,
tracing through your logic, and comparing actual vs expected output.
"""


# Quick comparison of all three
"""
Error Type         When it's Found              Program Crashes?      Example
Syntax Error        Before running (immediately)   Yes, won't run at all   Missing colon :
Runtime Error         While running, at that line     Yes, at that point      Division by zero
Logical Error          Never shown automatically        No, runs "fine"        Wrong formula/logic
"""


# A note on Python's error messages (Traceback)
"""
When a runtime error occurs, Python shows you a "Traceback" - a report of
exactly what happened and where. As a beginner, don't be intimidated by it -
read it from the BOTTOM UP:
    - The last line usually tells you the ERROR TYPE and a short message
    - The lines above it show you the PATH the program took to get there
Learning to read tracebacks calmly is one of the most useful debugging
skills you'll build early on.
"""