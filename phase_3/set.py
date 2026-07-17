# Here we'll cover the python set in detail
# set is a collection type in python which is used to store collection of UNIQUE data
# Example: s = {1,2,3,4,5}
# set is mutable data type (you can add/remove items)
# set is UNORDERED data type (no guaranteed order, may print in a different order than you typed)
# set does NOT allow duplicate values (duplicates are automatically removed)
# set does NOT support indexing or slicing (since it's unordered)
# set is a collection of heterogeneous data types (but items must be hashable/immutable)


# How to create a set
set1 = {1, 2, 3, 4, 5}                                  # set of integers
set2 = {"apple", "banana", "cherry"}                    # set of strings
set3 = {1, 2, 3, 4, 5, "apple", "banana", "cherry"}      # set of integers and strings
set4 = set()                                            # Empty set (NOTE: {} creates an empty dict, NOT a set!)
set5 = {1, "hello", 3.14, True}                          # set with different data types
set6 = {1, 2, 2, 3, 3, 3}                                 # duplicates are automatically removed
print(set6)  # {1, 2, 3}

print(type({}))    # <class 'dict'>  -> common beginner mistake
print(type(set4))  # <class 'set'>


# Sets have NO indexing (this would raise TypeError: 'set' object is not subscriptable)
set1 = {1, 2, 3, 4, 5}
# print(set1[0])   # NOT ALLOWED


# Add items to a set
set1 = {1, 2, 3}
set1.add(4)
print(set1)   # add() adds a single item

set1.update([5, 6, 7])
print(set1)   # update() adds multiple items from another iterable

set1.update({8, 9}, [10, 11])
print(set1)   # update() can take multiple iterables at once


# Remove items from a set
set1 = {1, 2, 3, 4, 5}

set1.remove(3)      # remove() deletes the value; raises KeyError if value doesn't exist
print(set1)

set1.discard(100)    # discard() deletes the value; does NOT raise an error if it doesn't exist
print(set1)          # this is the safer way to remove an item

a = set1.pop()         # pop() removes and returns a RANDOM item (sets are unordered)
print(a)
print(set1)

set1.clear()             # clear() empties the set
print(set1)              # set()


# Set operations (mathematical set theory)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A.union(B))            # or A | B    -> all items from both sets
print(A | B)

print(A.intersection(B))     # or A & B    -> items common to both sets
print(A & B)

print(A.difference(B))       # or A - B    -> items in A but NOT in B
print(A - B)

print(A.symmetric_difference(B))  # or A ^ B  -> items in A or B but NOT in both
print(A ^ B)

C = {1, 2}
print(C.issubset(A))       # True  -> is every item of C also in A?
print(A.issuperset(C))     # True  -> does A contain every item of C?

D = {100, 200}
print(A.isdisjoint(D))     # True  -> True if A and D have NO items in common


# Frozenset - an IMMUTABLE version of a set
fs = frozenset([1, 2, 3])
print(fs)
# fs.add(4)     # this would raise AttributeError, frozensets can't be changed


# Searching in a set
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

if 1000 in s:
    print("Present")
else:
    print("Not Present")

if 2 not in s:
    print("Not Present")
else:
    print("Present")