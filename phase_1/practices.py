# here are the practices for the phase_1 of the python course

"""
=========================================
          BEST PRACTICES
=========================================
1. Variable Naming: Always use meaningful and descriptive names. Use snake_case (e.g., student_name).
2. Comments: Use comments (#) to explain the purpose of your code, making it easier to read later.
3. Data Types: Always be aware of the data type you are working with. Use type() to verify.
4. User Input: Remember that input() always returns a string. Cast it to int() or float() if you need to perform mathematical operations.
5. String Formatting: Prefer using f-strings (f"...") for combining variables and strings, as it is cleaner and more readable than concatenation (+).
6. Slicing: Pay attention to zero-based indexing and remember that the stop index is exclusive in string slicing.
"""

# =========================================
#             PRACTICE QUESTIONS
# =========================================

"""
Question 1: Variables & Datatypes
Create variables for a student's name, age, and a boolean indicating if they are enrolled. 
Print their types and a formatted string (using f-string) containing their information.
"""

"""
Question 2: Input & Type Casting
Ask the user for their birth year, calculate their current age (assuming the current year is 2026), and print it.
"""

"""
Question 3: Operators
Take two numbers as input from the user. Print their sum, difference, product, and check if the first is greater than the second.
"""

"""
Question 4: String Slicing & Methods
Given a string text = "python programming", extract the word "python", print it in uppercase, and check if "pro" is in the string.
"""

"""
Question 5: Assignment & Logical Operators
Create a variable `score = 50`. Increase it by 20 using an assignment operator (+=). 
Check if the score is greater than 60 AND less than 100 using logical operators. 
Print the final score and the boolean result.
"""

"""
Question 6: String formatting & Identity Operators
Create two variables str1 = "hello" and str2 = "hello". 
Print a formatted string saying "String 1 is: <str1> and String 2 is: <str2>". 
Then check if str1 is str2 using the identity operator (is).
"""

"""
Question 7: Advanced String Slicing & Membership
Given sentence = "learning python is fun". 
Extract "python" using slicing. Then check if the letter "z" is NOT in the sentence using a membership operator.
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# name = "Ali"
# age = 20
# is_enrolled = True

# print(type(name))
# print(type(age))
# print(type(is_enrolled))
# print(f"Student {name} is {age} years old. Enrolled: {is_enrolled}")


# --- Solution 2 ---
# birth_year = int(input("Enter your birth year : "))
# current_year = 2026
# age = current_year - birth_year
# print("Your age is", age)


# --- Solution 3 ---
# num1 = float(input("Enter first number : "))
# num2 = float(input("Enter second number : "))

# print("Sum:", num1 + num2)
# print("Difference:", num1 - num2)
# print("Product:", num1 * num2)
# print("Is num1 greater than num2?", num1 > num2)


# --- Solution 4 ---
# text = "python programming"
# word = text[0:6]
# print(word.upper())
# print("pro" in text)


# --- Solution 5 ---
# score = 50
# score += 20
# print("Final score:", score)
# print("Is score between 60 and 100?", (score > 60) and (score < 100))


# --- Solution 6 ---
# str1 = "hello"
# str2 = "hello"
# print(f"String 1 is: {str1} and String 2 is: {str2}")
# print("Are they identical?", str1 is str2)


# --- Solution 7 ---
# sentence = "learning python is fun"
# python_word = sentence[9:15]
# print("Extracted word:", python_word)
# print("Is 'z' not in sentence?", "z" not in sentence)
