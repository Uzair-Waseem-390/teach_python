# Here we'll cover the python while loop in detail
# while loop repeats a block of code AS LONG AS a condition is True
# used when we don't know in advance how many times we need to repeat
# the condition is checked BEFORE every iteration (entry-controlled loop)
# if the condition is False on the very first check, the loop body never runs


# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1     # IMPORTANT: without updating count, this would be an infinite loop
print("Loop ended, count is now", count)


# while loop with user input (keep asking until correct)
"""
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted")
"""


# Infinite loop (demonstration only - commented out so this file doesn't hang)
"""
while True:
    print("This runs forever unless we break out of it")
"""


# while loop counting down
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast off!")


# while loop with break - stop the loop early when a condition is met
i = 0
while i < 10:
    if i == 5:
        break          # exits the loop immediately, skipping the rest
    print(i)
    i += 1


# while loop with continue - skip the current iteration, go to the next check
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue        # skip printing even numbers
    print(i)


# while-else - the else block runs ONLY IF the loop finished WITHOUT hitting a break
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop completed normally (no break happened)")

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("This will NOT print because the loop was broken")


# Common mistake: forgetting to update the loop variable -> infinite loop
"""
count = 0
while count < 5:
    print(count)
    # forgot count += 1 here -> this loop NEVER ends
"""


# do-while loop
"""
Some languages (like C, C++, Java) have a special "do-while" loop:
    - it runs the loop body FIRST, and checks the condition AFTER
    - this guarantees the body runs at least ONCE, even if the condition is False
      from the very start

Python does NOT have a built-in do-while keyword.
A normal while loop checks the condition BEFORE running the body (entry-controlled),
so if the condition is False on the first check, the body never runs even once.

We simulate a do-while loop in Python using: while True + break
"""

# do-while style loop -> runs at least once, then checks the condition
while True:
    num = 7
    print("This runs at least once, num =", num)
    if num > 5:      # the "condition" is checked AFTER the body has already run
        break         # exit once the condition is satisfied


# Practical example - keep asking for input until it's valid (do-while pattern)
"""
while True:
    age = input("Enter your age: ")
    if age.isdigit():          # runs at least once before we ever check the input
        print("Valid age:", age)
        break
    print("Invalid input, try again")
"""


# do-while vs normal while
"""
while (normal)        -> condition checked BEFORE the body -> body may run ZERO times
do-while (simulated)  -> condition checked AFTER the body  -> body runs AT LEAST ONCE

Python's while True + break inside is the standard idiom used to get do-while behavior.
"""