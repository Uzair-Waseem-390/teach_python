# Here we'll cover the python list in detail
# list is a collection type in python which is used to store collection of data
# Example: lis = [1,2,3,4,5]
# list is mutable data type
# list is ordered data type
# list allows duplicate values
# list allows indexing
# list is a collection of heterogeneous data types


# How to create a list
lis1 = [1, 2, 3, 4, 5]                                 # list of integers
lis2 = ["apple", "banana", "cherry"]                   # list of strings
lis3 = [1, 2, 3, 4, 5, "apple", "banana", "cherry"]    # list of integers and strings
lis4 = []                                              # Empty list
lis5 = list()                                          # Empty list using list constructor
lis6 = [1, "hello", 3.14, True]                        # list with different data types (heterogeneous)
lis7 = [[1, 2], [3, 4], [5, 6]]                         # Nested list


# How to access list items
lis1 = [1, 2, 3, 4, 5]
print(lis1[0])   # First item
print(lis1[1])   # Second item
print(lis1[2])   # Third item
print(lis1[3])   # Fourth item
print(lis1[4])   # Fifth item
print(lis1[-1])  # Last item
print(lis1[-2])  # Second last item
a = lis1[1]
print(a)  # Print the value of second item


# Change list items
lis1 = [1, 2, 3, 4, 5]
lis1[0] = 10
print(lis1)  # change the value of first item

list2 = ["banana", "cherry", "mango"]
list2[2] = "orange"
print(list2)  # change the value of third item


# Add list items
lis1 = [1, 2, 3, 4, 5]
lis1.append(6)
lis1.append("hello")
print(lis1)   # append() adds a single item to the end of the list

lis1.insert(1, 10)
print(lis1)   # insert() adds an item at a specific index

lis1.extend([11, 12, 13])
print(lis1)   # extend() adds each item of another iterable to the end

lis1.insert(len(lis1), 14)
print(lis1)   # inserting at len(lis1) has the same effect as append()


# Slicing a list
lis1 = [1, 2, 3, 4, 5]
print(lis1[1:3])    # Slicing a list from index 1 to 3 (exclusive)
print(lis1[:3])     # Slicing a list from index 0 to 3 (exclusive)
print(lis1[3:])     # Slicing a list from index 3 to the end
print(lis1[::2])    # Slicing a list with a step of 2
a = lis1[::-1]
print(a)  # Reverse a list using slicing


# List Concatenation
lis1 = lis1 + [15, 16, 17]  # Concatenate two lists (creates a new list)
print(lis1)


# List methods
lis1 = [1, 2, 3, 4, 5, 6, 7]

print(lis1.index(2))   # Index of the first occurrence of value 2
a = lis1.index(1)
print(a)

print(lis1.count(2))   # Count how many times value 2 appears
a = lis1.count(1)
print(a)

a = lis1.copy()         # copy() returns a new list, so we must store it in a variable
print(a)                # NOTE: copy() does NOT print/return anything useful on its own,
                         # that's why we don't do print(lis1.copy()) and use it directly

a = lis1.pop()          # pop() removes and returns the LAST item
print(a)                # 7
print(lis1)

a = lis1.pop(0)          # pop(0) removes and returns the item at index 0
print(a)                 # 1
print(lis1)

lis1.remove(3)            # remove() deletes the first matching VALUE (not index)
print(lis1)               # NOTE: remove() returns None, so never do print(lis1.remove(x))

lis1.sort()                # sort() sorts the list IN PLACE and returns None
print(lis1)                # that's why we call sort() then print(lis1) separately

lis1.reverse()              # reverse() reverses the list IN PLACE and returns None
print(lis1)

a = sorted(lis1)             # sorted() is a BUILT-IN FUNCTION (not a list method!)
print(a)                     # it returns a NEW sorted list, original list is unchanged
print(lis1)                  # lis1 itself is still in its previous (reversed) order


# Difference between del, pop() and remove()
"""
del        -> a keyword/statement, deletes by INDEX, can also delete the whole variable, returns nothing
pop()      -> a method, removes by INDEX (default last), RETURNS the removed item
remove()   -> a method, removes by VALUE (first match), returns None
"""

lis1 = [10, 20, 30, 40, 50]

del lis1[2]        # Delete the item at index 2 (30)
print(lis1)

del lis1            # Delete the entire list variable
# print(lis1)        # this would now raise a NameError since lis1 no longer exists

lis1 = [10, 20, 30, 40, 50]
a = lis1.pop()       # Remove and return the last item
print(a)
print(lis1)

a = lis1.pop(0)      # Remove and return the item at index 0
print(a)
print(lis1)

lis1.remove(30)       # Remove the value 30 (returns None)
print(lis1)

lis1.clear()           # clear() empties the list IN PLACE, returns None
print(lis1)            # []


# Searching in list
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if 1000 in lis:
    print("Present")
else:
    print("Not Present")

if 2 not in lis:
    print("Not Present")
else:
    print("Present")