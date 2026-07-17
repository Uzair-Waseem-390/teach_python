# Here we'll cover loop control statements in detail: break, continue, pass
# these statements change the normal flow of a loop


# break - immediately EXITS the loop entirely, no more iterations happen
for i in range(10):
    if i == 5:
        break
    print(i)
print("Loop stopped early using break")


# continue - SKIPS the rest of the current iteration and moves to the next one
for i in range(10):
    if i % 2 == 0:
        continue     # skip even numbers, don't print them
    print(i)


# pass - does absolutely NOTHING, it's just a placeholder
# used when a statement is syntactically required but you don't want any code to run yet
for i in range(5):
    if i == 3:
        pass          # TODO: handle this case later, for now do nothing
    print(i)


# Difference between break, continue and pass
"""
break     -> stops the loop completely, jumps OUT of the loop
continue  -> stops the CURRENT iteration only, jumps to the NEXT iteration
pass      -> does nothing at all, just a placeholder, loop continues normally
"""


# Common use case for pass - stub functions/loops while still writing code
def process_data(data):
    pass    # not implemented yet, but this lets the code run without an error


# Common use case for break - search and stop once found
numbers = [4, 8, 15, 16, 23, 42]
target = 16
for num in numbers:
    if num == target:
        print("Found:", target)
        break
else:
    print("Not found")   # for-else: runs only if break was never hit


# Common use case for continue - filter out unwanted items while looping
names = ["Ali", "", "Sara", None, "Ahmed"]
for name in names:
    if not name:            # skip empty strings and None values
        continue
    print(name)


# break and continue only affect the loop they are directly written inside
for i in range(3):
    for j in range(3):
        if j == 1:
            continue   # only skips the inner loop's current iteration
        print("i =", i, "j =", j)