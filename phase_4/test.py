# =========================================
#             TEST QUESTIONS
# =========================================

"""
Test 1: while Loop
Ask the user to enter numbers one at a time. Keep asking and adding them to a
running total until the user enters 0. Print the final total.
"""


"""
Test 2: for Loop
Print all the odd numbers between 1 and 20 (inclusive) using a for loop and range().
"""


"""
Test 3: Nested Loop
Print a multiplication table from 1x1 to 5x5 using a nested for loop, with each
row on its own line.
"""


"""
Test 4: break and continue
Loop through numbers 1 to 20. Skip (continue) any number divisible by 3, and stop
the loop completely (break) as soon as you reach a number greater than 15.
"""


"""
Test 5: do-while Style Loop
Simulate a do-while loop using while True + break: keep asking the user to enter
a password until they enter "python123". The prompt must run at least once even
if you could otherwise predict the outcome.
"""


"""
Test 6: Comprehension
Given a list of numbers [1,2,3,4,5,6,7,8,9,10], use a list comprehension to create
a new list containing only the squares of the EVEN numbers.
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# total = 0
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#     total += num
# print("Total:", total)


# --- Solution 2 ---
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)


# --- Solution 3 ---
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i * j, end=" ")
#     print()


# --- Solution 4 ---
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     if i > 15:
#         break
#     print(i)


# --- Solution 5 ---
# while True:
#     password = input("Enter password: ")
#     if password == "python123":
#         print("Access granted")
#         break
#     print("Wrong password, try again")


# --- Solution 6 ---
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_squares = [n * n for n in numbers if n % 2 == 0]
# print(even_squares)