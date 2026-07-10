# here are the practices for the phase_2 of the python course

"""
=========================================
          BEST PRACTICES
=========================================
1. if / elif / else: Always handle all possible cases. Use elif instead of multiple
   separate if statements when the conditions are mutually exclusive.
2. Indentation: Python uses indentation to define blocks. Be consistent — always use
   4 spaces per level. Never mix tabs and spaces.
3. Conditions: Keep conditions readable. Use parentheses to group complex conditions
   and avoid deeply nested logic when a simpler structure works.
4. Nested if: Limit nesting to 2–3 levels. If you're going deeper, consider refactoring
   your logic.
5. match-case: Use match-case (Python 3.10+) when comparing a single variable against
   multiple fixed values. It is cleaner than long if-elif chains.
6. Conditional Expression (Ternary): Use it for simple, one-line decisions.
   Avoid using it for complex logic — it hurts readability.
"""

# =========================================
#             PRACTICE QUESTIONS
# =========================================

"""
Question 1: if Statement
Ask the user to enter a number. If the number is positive, print "The number is positive".
If the number is negative, print "The number is negative". If it is zero, print "The number is zero".
(Use separate if statements, not elif)
"""

"""
Question 2: if-else Statement
Ask the user to enter their marks (0–100). If marks are 50 or above, print "Pass".
Otherwise, print "Fail".
"""

"""
Question 3: elif Chain
Ask the user to enter a temperature in Celsius and classify it:
- Below 0   -> "Freezing"
- 0 to 15   -> "Cold"
- 16 to 25  -> "Comfortable"
- 26 to 35  -> "Warm"
- Above 35  -> "Hot"
"""

"""
Question 4: Nested if
Ask the user for their age and whether they have a driving license (yes/no).
- If age >= 18 AND has license -> "You can drive."
- If age >= 18 but no license  -> "You need a license to drive."
- If age < 18                  -> "You are too young to drive."
"""

"""
Question 5: match-case
Ask the user to enter a number from 1 to 7. Use match-case to print the name of the
corresponding day of the week. If the number is invalid, print "Invalid day".
"""

"""
Question 6: Conditional Expression (Ternary)
Ask the user for a number. In a single line, assign "Even" to a variable if the number
is divisible by 2, otherwise assign "Odd". Print the result.
"""

"""
Question 7: Combined — All Concepts
Ask the user to enter their score (0–100) and their attendance percentage.
- If score >= 50 and attendance >= 75 -> "Pass and eligible for certificate."
- If score >= 50 but attendance < 75  -> "Pass but attendance is low."
- If score < 50 and attendance >= 75  -> "Failed despite good attendance."
- If score < 50 and attendance < 75   -> "Failed and low attendance."
Also, use a conditional expression to print "Merit" if the score is 85 or above, else "Normal".
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive")
# if num < 0:
#     print("The number is negative")
# if num == 0:
#     print("The number is zero")


# --- Solution 2 ---
# marks = int(input("Enter your marks: "))
# if marks >= 50:
#     print("Pass")
# else:
#     print("Fail")


# --- Solution 3 ---
# temp = float(input("Enter temperature in Celsius: "))
# if temp < 0:
#     print("Freezing")
# elif temp <= 15:
#     print("Cold")
# elif temp <= 25:
#     print("Comfortable")
# elif temp <= 35:
#     print("Warm")
# else:
#     print("Hot")


# --- Solution 4 ---
# age = int(input("Enter your age: "))
# has_license = input("Do you have a driving license? (yes/no): ").lower()
# if age >= 18:
#     if has_license == "yes":
#         print("You can drive.")
#     else:
#         print("You need a license to drive.")
# else:
#     print("You are too young to drive.")


# --- Solution 5 ---
# day = int(input("Enter a number (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")


# --- Solution 6 ---
# num = int(input("Enter a number: "))
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)


# --- Solution 7 ---
# score = int(input("Enter your score: "))
# attendance = int(input("Enter your attendance %: "))
# if score >= 50:
#     if attendance >= 75:
#         print("Pass and eligible for certificate.")
#     else:
#         print("Pass but attendance is low.")
# else:
#     if attendance >= 75:
#         print("Failed despite good attendance.")
#     else:
#         print("Failed and low attendance.")
# status = "Merit" if score >= 85 else "Normal"
# print(status)
