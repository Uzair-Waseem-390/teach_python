# here we understand the match case working
# Python does not have a traditional switch statement like C, C++, Java, or C#.
# In Python, we usually use match-case (Python 3.10+) or multiple if-elif-else statements.


# syntex
# match variable:
    # case value1:
    #     code
    # case value2:
    #     code
    # case _:
    #     default code

# Here, _ acts like the default case.
# default case executes when no match is found (no other case is executed)

# Example 1: Basic match-case

day = int(input("Enter a day: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# Example 2: Traffic Light

light = input("Enter the light color: ").lower()
match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")


# Example 3: Simple Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print("Result: ", num1 + num2)
    case "-":
        print("Result: ", num1 - num2)
    case "*":
        print("Result: ", num1 * num2)
    case "/":
        print("Result: ", num1 / num2)
    case _:
        print("Invalid operator")


# Example 4: Check grade

grade = input("Enter your grade: ").upper()
match grade:
    case "A":
        print("Grade A: Excellent")
    case "B":
        print("Grade B: Very Good")
    case "C":
        print("Grade C: Good")
    case "D":
        print("Grade D: Average")
    case "F":
        print("Grade F: Fail")
    case _:
        print("You didn't pass in exam")