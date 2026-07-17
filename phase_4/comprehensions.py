# Here we'll cover comprehensions in detail
# comprehensions are a short, one-line way to create a list, set, or dictionary using a loop
# they combine a for loop (and optionally an if condition) into a single expression
# comprehensions are more compact and often faster than writing a full for loop with .append()


# ---------- List Comprehension ----------
# Normal way using a for loop
squares = []
for i in range(5):
    squares.append(i * i)
print(squares)

# Same thing using list comprehension
squares = [i * i for i in range(5)]
print(squares)   # syntax: [expression for item in iterable]


# List comprehension with a condition (filtering)
evens = [i for i in range(10) if i % 2 == 0]
print(evens)   # syntax: [expression for item in iterable if condition]


# List comprehension with if-else (this is a conditional EXPRESSION, not a filter)
labels = ["even" if i % 2 == 0 else "odd" for i in range(6)]
print(labels)   # syntax: [expr_if_true if condition else expr_if_false for item in iterable]


# List comprehension over a string
letters = [ch.upper() for ch in "python"]
print(letters)


# Nested list comprehension (equivalent to a nested for loop)
pairs = [(i, j) for i in range(3) for j in range(2)]
print(pairs)   # same result as the nested for loop in nested_loops.py

# Flattening a 2D list (matrix) using nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [value for row in matrix for value in row]
print(flat)


# ---------- Set Comprehension ----------
# Normal way using a for loop
unique_lengths = set()
for word in ["apple", "kiwi", "banana", "fig"]:
    unique_lengths.add(len(word))
print(unique_lengths)

# Same thing using set comprehension
unique_lengths = {len(word) for word in ["apple", "kiwi", "banana", "fig"]}
print(unique_lengths)   # syntax: {expression for item in iterable}
# NOTE: duplicates are automatically removed, since it's a set


# Set comprehension with a condition
odd_squares = {i * i for i in range(10) if i % 2 != 0}
print(odd_squares)


# ---------- Dictionary Comprehension ----------
# Normal way using a for loop
squares_dict = {}
for i in range(5):
    squares_dict[i] = i * i
print(squares_dict)

# Same thing using dict comprehension
squares_dict = {i: i * i for i in range(5)}
print(squares_dict)   # syntax: {key_expr: value_expr for item in iterable}


# Dict comprehension with a condition
names = ["Ali", "Sara", "Ahmed", "Zoya"]
name_lengths = {name: len(name) for name in names if len(name) > 3}
print(name_lengths)


# Dict comprehension swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(swapped)


# When to use comprehensions vs a normal loop
"""
Use a comprehension when:
    - the logic is simple (one expression, maybe one condition)
    - it makes the code shorter and easier to read

Use a normal for loop when:
    - the logic is complex (multiple steps, multiple conditions, side effects like printing)
    - a comprehension would become hard to read (avoid deeply nested comprehensions)
"""