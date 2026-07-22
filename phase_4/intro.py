"""
In Phase 4 we study Loops
1. while loop
2. for loop
3. nested loops
4. loop control statements (break, continue, pass)
5. loop else
6. comprehensions (list, dict, set)

Loops are used to execute a block of code repeatedly.
"""


# Why we need loops
"""
In Phase 2 we learned conditional statements (if, if-else, elif) which let the program
make a DECISION and run some code ONCE based on a condition.

But what if we want to run the SAME piece of code many times?
Example: print "Hello" 100 times, or print every number from 1 to 1000,
or ask the user for a password until they get it right.

Without loops we would have to write the same line of code again and again:
    print("Hello")
    print("Hello")
    print("Hello")
    ... 100 times   <-- not practical at all

Loops solve this problem. They let us repeat a block of code:
    - a fixed number of times
    - once for every item in a collection (list, tuple, set, dict, string)
    - until a certain condition becomes False
"""


# What problems do loops solve
"""
1. Repetition       -> running the same code multiple times without duplicating it
2. Iteration        -> going through every item of a list/tuple/set/dict/string one by one
3. Automation        -> doing repetitive tasks like validating input, processing files, etc.
4. Searching          -> checking each item of a collection to find something
5. Counting/Summing    -> keep a running total or count while going through data
"""


# Two main types of loops in Python
"""
Loop Type      Best used when...
1. while       you don't know in advance HOW MANY times to repeat - repeat UNTIL a condition
               becomes False (example: keep asking for input until it's valid)

2. for         you know you want to go through a SEQUENCE / collection, or repeat a KNOWN
               number of times (example: print each name in a list, print numbers 1 to 10)
"""


# A quick preview (we'll cover each of these in detail in separate files)
for i in range(3):
    print("for loop iteration:", i)

count = 0
while count < 3:
    print("while loop iteration:", count)
    count += 1

print("after loop")