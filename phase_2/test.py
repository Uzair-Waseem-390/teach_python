# =========================================
#             TEST QUESTIONS
# =========================================

"""
Test 1: if Statement
Ask the user to enter their age. Using only if statements (no else/elif),
print "Child" if age is below 13, "Teenager" if age is between 13 and 17,
and "Adult" if age is 18 or above.
"""


"""
Test 2: if-else Statement
Ask the user to enter a username. If the username equals "admin" (case-insensitive),
print "Welcome, Admin!". Otherwise, print "Access Denied."
"""


"""
Test 3: elif Chain
Ask the user to enter a score and print the grade:
- 90 and above  -> "A+"
- 80 to 89      -> "A"
- 70 to 79      -> "B"
- 60 to 69      -> "C"
- 50 to 59      -> "D"
- Below 50      -> "F"
"""


"""
Test 4: Nested if
Ask the user for their account balance and how much they want to withdraw.
- If balance is greater than 0:
    - If the withdrawal amount is less than or equal to the balance, print
      "Withdrawal successful." and the remaining balance.
    - Otherwise, print "Insufficient balance."
- If balance is 0 or less, print "Invalid balance."
"""


"""
Test 5: match-case
Ask the user to enter a math operator (+, -, *, /). Use match-case to print
what that operator does (e.g., "+" -> "Addition"). For anything else, print "Unknown operator".
"""


"""
Test 6: Conditional Expression (Ternary)
Ask the user to enter two numbers. Using a single conditional expression,
print "First is greater" if the first number is larger, otherwise print "Second is greater or equal".
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# age = int(input("Enter your age: "))
# if age < 13:
#     print("Child")
# if 13 <= age <= 17:
#     print("Teenager")
# if age >= 18:
#     print("Adult")


# --- Solution 2 ---
# username = input("Enter your username: ")
# if username.lower() == "admin":
#     print("Welcome, Admin!")
# else:
#     print("Access Denied.")


# --- Solution 3 ---
# score = int(input("Enter your score: "))
# if score >= 90:
#     print("A+")
# elif score >= 80:
#     print("A")
# elif score >= 70:
#     print("B")
# elif score >= 60:
#     print("C")
# elif score >= 50:
#     print("D")
# else:
#     print("F")


# --- Solution 4 ---
# balance = int(input("Enter your balance: "))
# amount = int(input("Enter withdrawal amount: "))
# if balance > 0:
#     if amount <= balance:
#         print("Withdrawal successful.")
#         print("Remaining balance:", balance - amount)
#     else:
#         print("Insufficient balance.")
# else:
#     print("Invalid balance.")


# --- Solution 5 ---
# op = input("Enter an operator (+, -, *, /): ")
# match op:
#     case "+":
#         print("Addition")
#     case "-":
#         print("Subtraction")
#     case "*":
#         print("Multiplication")
#     case "/":
#         print("Division")
#     case _:
#         print("Unknown operator")


# --- Solution 6 ---
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# result = "First is greater" if num1 > num2 else "Second is greater or equal"
# print(result)
