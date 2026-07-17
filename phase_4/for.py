# Here we'll cover the python for loop in detail
# for loop is used to iterate over a SEQUENCE (list, tuple, set, dict, string) or range()
# used when we know we want to go through every item of a collection,
# or repeat a KNOWN number of times
# for loop is generally preferred over while loop when the number of iterations is known


# for loop with range()
for i in range(5):          # range(5) -> 0,1,2,3,4  (5 is excluded)
    print(i)

for i in range(2, 6):        # range(start, stop) -> 2,3,4,5
    print(i)

for i in range(0, 10, 2):     # range(start, stop, step) -> 0,2,4,6,8
    print(i)

for i in range(10, 0, -1):     # negative step -> counts backwards, 10,9,...,1
    print(i)


# for loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# for loop over a tuple
coordinates = (10, 20, 30)
for value in coordinates:
    print(value)


# for loop over a set (order is not guaranteed since sets are unordered)
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    print(num)


# for loop over a string - iterates character by character
for ch in "Python":
    print(ch)


# for loop over a dictionary - iterates over KEYS by default
student = {"name": "Ali", "age": 20, "city": "Lahore"}
for key in student:
    print(key)

for key, value in student.items():   # iterate key:value pairs together
    print(key, ":", value)


# for loop with enumerate() - get both index and value while looping
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, start=1):   # start counting from 1 instead of 0
    print(index, fruit)


# for loop with zip() - loop through two (or more) sequences together, pairwise
names = ["Ali", "Sara", "Ahmed"]
ages = [20, 22, 25]
for name, age in zip(names, ages):
    print(name, "is", age, "years old")


# for loop with break - stop the loop early
for i in range(10):
    if i == 5:
        break
    print(i)


# for loop with continue - skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # only prints odd numbers


# for-else - the else block runs ONLY IF the loop finished WITHOUT hitting a break
for i in range(5):
    print(i)
else:
    print("Loop completed normally (no break happened)")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print because the loop was broken")


# for loop vs while loop
"""
Use for   -> when looping over a known collection / known range of numbers
Use while -> when looping until a condition becomes False, and you don't know
             the exact number of iterations in advance
"""