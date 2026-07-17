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