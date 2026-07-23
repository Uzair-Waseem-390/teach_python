# here are the practices for the phase_3 of the python course

"""
=========================================
          BEST PRACTICES
=========================================
1. Choosing the right collection: Use a list when order + duplicates + changeability
   matter. Use a tuple for fixed data that shouldn't change. Use a set when you only
   care about uniqueness and don't need order. Use a dictionary when you need to
   look values up by a meaningful key instead of a numeric index.
2. Mutability awareness: Remember lists/sets/dicts are mutable, tuples are not.
   Don't try to modify a tuple in place — rebuild it instead.
3. Method return values: Methods like sort(), reverse(), remove(), clear(), update()
   return None. Never do print(my_list.sort()) — call the method, then print separately.
4. sorted() vs .sort(): sorted() works on any iterable and returns a NEW list.
   .sort() only works on lists, sorts in place, and returns None.
5. Safe access: Prefer dict.get(key, default) over dict[key] when a key might not
   exist, to avoid a KeyError crashing your program.
6. Comprehensions (once learned): Prefer a comprehension over a manual loop + append
   when building a simple new list/set/dict from an existing iterable.
"""

# =========================================
#             PRACTICE QUESTIONS
# =========================================

"""
Question 1: List Slicing
Create a list of numbers from 1 to 10. Print the first 3 numbers, the last 3 numbers,
and every 2nd number using slicing.
"""
list=[1,2,3,4,5,6,7,8,9,10]
print(list[0:3:])
print(list[-4:-1])


"""
Question 2: List Methods
Create a list of 5 city names. Use .index() to find the position of one city,
.count() to count how many times a city appears, and .copy() to make a duplicate
of the list. Print all three results.
"""
list=["lahore", "faisalabad", "karachi", "multan", "islamabad"]
print(list.index("islamabad"))
print(list.count("lahore"))
list2=(list.copy())
print(list2)
"""
Question 3: Tuple Unpacking
Create a tuple with 4 subject names. Unpack the first two subjects into separate
variables and the remaining two into a single variable using * unpacking.
Print all the variables.
"""

"""
Question 4: Set Uniqueness
Ask the user to enter 10 numbers one by one (using a loop or input().split()).
Store them in a set and print how many UNIQUE numbers were entered.
"""

"""
Question 5: Dictionary Loop
Create a dictionary of 5 products with their prices. Loop through the dictionary
and print each product name along with its price in the format:
"Product: <name>, Price: <price>"
"""

"""
Question 6: Dictionary Update
Create a dictionary representing a shopping cart (item: quantity). Ask the user
for an item name and a quantity. If the item already exists, increase its quantity.
If it doesn't exist, add it as a new item. Print the updated cart.
"""

"""
Question 7: Combined — All Concepts
Create a list of student names, a tuple of possible grades ("A","B","C","D","F"),
a set to track which grades have actually been given out, and a dictionary mapping
each student name to their grade. Loop through the students, assign each one a
grade of your choice, add that grade to the set, and store it in the dictionary.
At the end, print the dictionary and the set of grades that were actually used.
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# numbers = list(range(1, 11))
# print("First 3:", numbers[:3])
# print("Last 3:", numbers[-3:])
# print("Every 2nd:", numbers[::2])


# --- Solution 2 ---
# cities = ["Lahore", "Karachi", "Multan", "Lahore", "Quetta"]
# print("Index of 'Multan':", cities.index("Multan"))
# print("Count of 'Lahore':", cities.count("Lahore"))
# cities_copy = cities.copy()
# print("Copy:", cities_copy)


# --- Solution 3 ---
# subjects = ("Math", "Physics", "Chemistry", "Biology")
# first, second, *rest = subjects
# print(first)
# print(second)
# print(rest)


# --- Solution 4 ---
# entered = input("Enter 10 numbers separated by space: ").split()
# unique_numbers = set(entered)
# print("Unique numbers entered:", len(unique_numbers))


# --- Solution 5 ---
# products = {"Pen": 10, "Notebook": 50, "Bag": 800, "Bottle": 150, "Shoes": 2500}
# for name, price in products.items():
#     print(f"Product: {name}, Price: {price}")


# --- Solution 6 ---
# cart = {"Apple": 3, "Bread": 1}
# item = input("Enter item name: ")
# qty = int(input("Enter quantity: "))
# if item in cart:
#     cart[item] += qty
# else:
#     cart[item] = qty
# print(cart)


# --- Solution 7 ---
# students = ["Ali", "Sara", "Ahmed", "Zoya"]
# possible_grades = ("A", "B", "C", "D", "F")
# grades_used = set()
# student_grades = {}
#
# chosen_grades = ["A", "B", "A", "C"]   # example grade for each student in order
# for student, grade in zip(students, chosen_grades):
#     student_grades[student] = grade
#     grades_used.add(grade)
#
# print(student_grades)
# print(grades_used)