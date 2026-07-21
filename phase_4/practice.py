# here are the practices for the phase_4 of the python course

"""
=========================================
          BEST PRACTICES
=========================================
1. Choosing while vs for: Use for when looping over a known collection or a known
   range. Use while when repeating until a condition changes, especially when you
   don't know the number of iterations in advance.
2. Avoid infinite loops: Always make sure the while loop's condition can eventually
   become False (update the loop variable / have a break with a real exit condition).
3. break vs continue: Use break to stop the loop completely, continue to skip just
   the current iteration. Don't overuse either — too many can make logic hard to follow.
4. Nested loops: Be mindful of performance — a loop inside a loop runs inner_count *
   outer_count times. Keep nesting to 2-3 levels max, refactor into functions if deeper.
5. Loop variables: Give loop variables meaningful names (row, col, student) instead
   of always i, j, k, especially in nested loops, to keep the code readable.
6. Comprehensions: Great for simple transformations/filters. If the logic needs
   multiple conditions or steps, a normal loop is more readable — don't force it.
"""

# =========================================
#             PRACTICE QUESTIONS
# =========================================

"""
Question 1: while Loop - Countdown
Ask the user for a starting number and count down to 0 using a while loop,
printing each number. After reaching 0, print "Liftoff!".
"""

"""
Question 2: for Loop - Sum and Average
Ask the user to enter 5 numbers using a for loop with range(). Keep a running
total, then print the sum and the average of the 5 numbers.
"""

"""
Question 3: Nested Loop - Pattern Printing
Using nested loops, print a right-angled triangle of stars for a given number
of rows (e.g., 5 rows), where row i has i stars.
"""

"""
Question 4: break - Search in a List
Ask the user for a name to search for in a list of names. Loop through the list
and print "Found!" and stop searching as soon as it's found. If the loop finishes
without finding it, print "Not found." (hint: use for-else)
"""

"""
Question 5: continue - Filtering
Loop through a list of numbers from 1 to 30. Print only the numbers that are
divisible by both 3 and 5, skipping (using continue) all others.
"""

"""
Question 6: do-while Style - Menu Loop
Simulate a do-while loop that shows a menu (1. Add, 2. Subtract, 3. Exit) and
keeps showing it after every action, until the user chooses option 3 to exit.
"""

"""
Question 7: Combined — All Concepts
Ask the user to enter numbers one at a time (using a do-while style loop) until
they type "done". Store all VALID numbers in a list. Skip (continue) any input
that isn't a valid number instead of crashing. At the end, use a list comprehension
to create a new list containing only the numbers greater than 10, and print both
the original list and the filtered list.
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# start = int(input("Enter a starting number: "))
# while start >= 0:
#     print(start)
#     start -= 1
# print("Liftoff!")


# --- Solution 2 ---
# total = 0
# for i in range(5):
#     num = float(input(f"Enter number {i + 1}: "))
#     total += num
# print("Sum:", total)
# print("Average:", total / 5)


# --- Solution 3 ---
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()


# --- Solution 4 ---
# names = ["Ali", "Sara", "Ahmed", "Zoya"]
# target = input("Enter a name to search: ")
# for name in names:
#     if name == target:
#         print("Found!")
#         break
# else:
#     print("Not found.")


# --- Solution 5 ---
# for num in range(1, 31):
#     if not (num % 3 == 0 and num % 5 == 0):
#         continue
#     print(num)


# --- Solution 6 ---
# while True:
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Exit")
#     choice = input("Choose an option: ")
#     if choice == "1":
#         print("Adding...")
#     elif choice == "2":
#         print("Subtracting...")
#     elif choice == "3":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice, try again")


# --- Solution 7 ---
# valid_numbers = []
# while True:
#     entry = input("Enter a number (or 'done' to stop): ")
#     if entry.lower() == "done":
#         break
#     if not entry.isdigit():
#         print("Invalid number, skipping...")
#         continue
#     valid_numbers.append(int(entry))
#
# filtered = [n for n in valid_numbers if n > 10]
# print("All numbers:", valid_numbers)
# print("Numbers greater than 10:", filtered)