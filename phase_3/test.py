# =========================================
#             TEST QUESTIONS
# =========================================

"""
Test 1: List Basics
Create a list of 5 favorite movies. Print the first movie, the last movie,
and the total number of movies using len().
"""


"""
Test 2: List Modification
Take a list of numbers [10, 20, 30, 40, 50]. Add 60 to the end, insert 15 at
index 1, remove the value 30, and finally print the resulting list.
"""


"""
Test 3: Tuple Basics
Create a tuple containing your name, age, and city. Try to change the age
value directly (observe the error), then show the correct way to "update"
a tuple by converting it to a list, changing it, and converting it back.
"""


"""
Test 4: Set Operations
Create two sets: A = {1,2,3,4,5} and B = {4,5,6,7,8}.
Print their union, intersection, and difference (A - B).
"""


"""
Test 5: Dictionary Basics
Create a dictionary for a student with keys "name", "roll_no", and "marks".
Print the student's name using .get(), then update the marks value,
and finally add a new key "grade" with an appropriate value.
"""


"""
Test 6: Combined — Searching
Take a list of numbers, a tuple of fruits, a set of cities, and a dictionary
of student records. Ask the user for a value and check if it exists in EACH
of the four collections, printing a clear message for each one.
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# movies = ["Inception", "Interstellar", "The Matrix", "Gladiator", "Whiplash"]
# print("First movie:", movies[0])
# print("Last movie:", movies[-1])
# print("Total movies:", len(movies))


# --- Solution 2 ---
# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# numbers.insert(1, 15)
# numbers.remove(30)
# print(numbers)


# --- Solution 3 ---
# person = ("Ali", 20, "Lahore")
# print(person)
# # person[1] = 21   # TypeError: 'tuple' object does not support item assignment
# temp = list(person)
# temp[1] = 21
# person = tuple(temp)
# print(person)


# --- Solution 4 ---
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print("Union:", A | B)
# print("Intersection:", A & B)
# print("Difference (A - B):", A - B)


# --- Solution 5 ---
# student = {"name": "Sara", "roll_no": 21, "marks": 85}
# print(student.get("name"))
# student["marks"] = 90
# student["grade"] = "A"
# print(student)


# --- Solution 6 ---
# numbers = [10, 20, 30, 40]
# fruits = ("apple", "banana", "cherry")
# cities = {"Lahore", "Karachi", "Islamabad"}
# students = {"Ali": 85, "Sara": 90}
#
# value = input("Enter a value to search: ")
#
# if value.isdigit() and int(value) in numbers:
#     print("Found in numbers list")
# else:
#     print("Not found in numbers list")
#
# if value in fruits:
#     print("Found in fruits tuple")
# else:
#     print("Not found in fruits tuple")
#
# if value in cities:
#     print("Found in cities set")
# else:
#     print("Not found in cities set")
#
# if value in students:
#     print("Found as a key in students dictionary")
# else:
#     print("Not found in students dictionary")