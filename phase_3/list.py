# Here we'll cover the python list in detial
# list is a collection type in python which is used to store collection of data
# Example:list = [1,2,3,4,5]
# list is mutable data type
# list is ordered data type
# list allows duplicate values
# list allows indexing
# list is collection of hetrojenous data types


# How to create a list
lis1 = [1,2,3,4,5]       # list of integers
lis2 = ["apple", "banana", "cherry"]  # list of strings
lis3 = [1,2,3,4,5, "apple", "banana", "cherry"]  # list of integers and strings
lis4 = [] # Empty list
lis5 = list() # Empty list using list constructor
lis6 = [1, "hello", 3.14, True] # list with different data types or heterogeneous data types
lis7 = [[1,2], [3,4], [5,6]] # Nested list


# How to access list items
print(lis1[0])  # First item
print(lis1[1])  # Second item
print(lis1[2])  # Third item
print(lis1[3])  # Fourth item
print(lis1[4])  # Fifth item
print(lis1[-1]) # Last item
print(lis1[-2]) # Second last item
a = lis1[1]
print(a) # Print the value of second item


# Change list items
lis1[0] = 10
print(lis1)   # change the value of first item
list2 = ["banana", "cherry", "mango"]
list2[2] = "orange"
print(list2)  # change the value of first item





# Add list items
lis1.append(6)
print(lis1)   # add the value of 6 to the end of the list
lis1.insert(1, 10)
print(lis1)   # insert the value of 10 at index 1
lis1.extend([11,12,13])
print(lis1)   # extend the list with the values of 11, 12, 13
lis1.insert(len(lis1), 14)
print(lis1)   # insert the value of 14 at the end of the list




# Slicing a list
print(lis1[1:3]) # Slicing a list from index 1 to 3 (exclusive)
print(lis1[:3]) # Slicing a list from index 0 to 3 (exclusive)
print(lis1[3:]) # Slicing a list from index 3 to the end
print(lis1[1:3:5]) # Slicing a list with a step of 5
a = lis1[::-1]
print(a) # Reverse a list



# list methods
print(lis1.index(2)) # Index of the value 2
a = lis1.index(1)
print(a) # Print the index of value 1

print(lis1.count(2)) # Count the number of values 2
a = lis1.count(1)
print(a) # Print the count of value 1

print(lis1.copy()) # Copy the list
a = lis1.copy()
print(a) # Print the copy of the list

print(lis1.clear()) # Clear the list
a = lis1.clear()
print(a) # Print the cleared list

print(lis1.pop()) # Remove the last item
a = lis1.pop()
print(a) # Print the removed item

print(lis1.pop(0)) # Remove the item at index 0
a = lis1.pop(0)
print(a) # Print the removed item
print(lis1.remove(2)) # Remove the value 2

print(lis1.sort()) # Sort the list

print(lis1.reverse()) # Reverse the list

print(lis1.sorted()) # Return a sorted copy of the list
a = lis1.sorted()
print(a) # Print the sorted list