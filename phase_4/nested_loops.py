# Here we'll cover nested loops in detail
# a nested loop is a loop INSIDE another loop
# the inner loop runs COMPLETELY for every single iteration of the outer loop
# used for working with grids, tables, matrices, patterns, and comparing pairs of items


# Basic nested for loop
for i in range(3):            # outer loop -> runs 3 times
    for j in range(2):         # inner loop -> runs 2 times for EACH outer iteration
        print("i =", i, "j =", j)
# total prints = 3 * 2 = 6


# Nested loop - multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
    print("---")   # separator after each outer loop's inner loop finishes


# Nested loop - printing a simple pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")   # end="" keeps printing on the same line
    print()                  # move to the next line after the inner loop finishes

"""
Output:
*
**
***
****
*****
"""


# Nested loop over a nested list (2D list / matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# Nested loop with while
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print("i =", i, "j =", j)
        j += 1
    i += 1


# break inside a nested loop only breaks the INNERMOST loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break          # only exits the inner loop, outer loop continues
        print("i =", i, "j =", j)


# Using a flag variable to break out of BOTH loops when needed
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
    if found:
        break
print("Stopped at i =", i, "j =", j)