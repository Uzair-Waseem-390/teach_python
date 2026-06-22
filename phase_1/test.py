# =========================================
#             TEST QUESTIONS
# =========================================

"""
Test 1: Datatypes & Variables
Create a variable `city` and assign a string value to it. Create a variable `population` and assign an integer value. 
Check and print the data type of both variables.
"""


"""
Test 2: Input & Type Casting
Take a temperature in Celsius as input from the user (make sure to convert it to a float). 
Convert it to Fahrenheit using the formula (C * 9/5) + 32 and print the result.
"""


"""
Test 3: Arithmetic & Relational Operators
Create two variables x = 15 and y = 4. 
Find the remainder when x is divided by y. 
Then, check if x is perfectly divisible by y (i.e., if the remainder is 0) and print the boolean result.
"""


"""
Test 4: String Methods
Ask the user to input their full name. 
Print the length of their name. Then, print the name with the first letter of each word capitalized.
"""


"""
Test 5: Print Statement Formatting
Print the three strings "Python", "is", and "awesome" so that they are separated by hyphens ("-") 
and the output ends with an exclamation mark ("!"). 
Hint: use the `sep` and `end` arguments of the print function.
"""


# =========================================
#             SOLUTIONS
# =========================================

# --- Solution 1 ---
# city = "Lahore"
# population = 13000000

# print(type(city))
# print(type(population))


# --- Solution 2 ---
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Temperature in Fahrenheit is: {fahrenheit}")


# --- Solution 3 ---
# x = 15
# y = 4
# remainder = x % y

# print("Remainder:", remainder)
# print("Is x perfectly divisible by y?", remainder == 0)


# --- Solution 4 ---
# full_name = input("Enter your full name: ")

# print("Length of name:", len(full_name))
# print("Capitalized name:", full_name.title())


# --- Solution 5 ---
# print("Python", "is", "awesome", sep="-", end="!\n")
