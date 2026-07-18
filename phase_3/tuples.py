# Here we'll cover the python tuple in detail
# tuple is a collection type in python which is used to store collection of data
# Example: tup = (1,2,3,4,5)
# tuple is IMMUTABLE data type (cannot be changed after creation)
# tuple is ordered data type
# tuple allows duplicate values
# tuple allows indexing
# tuple is a collection of heterogeneous data types
# tuples are generally faster than lists and used for data that should NOT change


# How to create a tuple
tup1 = (1, 2, 3, 4, 5)                                  # tuple of integers
tup2 = ("apple", "banana", "cherry")                    # tuple of strings
tup3 = (1, 2, 3, 4, 5, "apple", "banana", "cherry")     # tuple of integers and strings
tup4 = ()                                               # Empty tuple
tup5 = tuple()                                          # Empty tuple using tuple constructor
tup6 = (1, "hello", 3.14, True)                         # tuple with different data types
tup7 = ((1, 2), (3, 4), (5, 6))                          # Nested tuple

single = (5,)     # a single item tuple MUST have a trailing common
not_a_tuple = (5)  # this is just an int in parentheses, NOT a tuple
print(type(single))       # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>
# exit()

# How to access tuple items
tup1 = (1, 2, 3, 4, 5)
print(tup1[0])   # First item
print(tup1[1])   # Second item
print(tup1[2])   # Third item
print(tup1[3])   # Fourth item
print(tup1[4])   # Fifth item
print(tup1[-1])  # Last item
print(tup1[-2])  # Second last item
a = tup1[1]
print(a)  # Print the value of second item


# Tuples are immutable - items CANNOT be changed
tup1 = (1, 2, 3, 4, 5)
# tup1[0] = 10        # this would raise: TypeError: 'tuple' object does not support item assignment

# Workaround: convert to list, change it, convert back to tuple
temp = list(tup1)
temp[0] = 10
tup1 = tuple(temp)
print(tup1)  # (10, 2, 3, 4, 5)


# "Adding" items to a tuple (tuples don't have append/insert/extend)
tup1 = (1, 2, 3)
tup1 = tup1 + (4, 5)   # Concatenation creates a brand NEW tuple
print(tup1)

tup1 = tup1 * 2         # Repetition also creates a brand NEW tuple
print(tup1)


# Slicing a tuple
tup1 = (1, 2, 3, 4, 5)
print(tup1[1:3])   # Slicing from index 1 to 3 (exclusive)
print(tup1[:3])    # Slicing from index 0 to 3 (exclusive)
print(tup1[3:])    # Slicing from index 3 to the end
print(tup1[::2])   # Slicing with a step of 2
a = tup1[::-1]
print(a)  # Reverse a tuple using slicing


# Tuple methods (tuples only have 2 methods, since they are immutable)
tup1 = (1, 2, 3, 2, 4, 2, 5)

print(tup1.count(2))   # Count how many times value 2 appears
a = tup1.count(2)
print(a)

print(tup1.index(3))   # Index of the first occurrence of value 3
a = tup1.index(4)
print(a)


# Tuple packing and unpacking
packed = 1, 2, 3               # packing: parentheses are optional
print(packed)
print(type(packed))            # <class 'tuple'>

a, b, c = packed                # unpacking: number of variables must match number of items
print(a, b, c)

first, *middle, last = (1, 2, 3, 4, 5)   # unpacking with * to grab the "rest"
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5


# Deleting a tuple
tup1 = (1, 2, 3)
del tup1              # del deletes the WHOLE tuple variable (individual items can't be deleted)
# print(tup1)          # this would now raise a NameError since tup1 no longer exists


# Searching in a tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

if 1000 in tup:
    print("Present")
else:
    print("Not Present")

if 2 not in tup:
    print("Not Present")
else:
    print("Present")