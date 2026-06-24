# here we understand the if statement
# it is used to make decision 
# for example if it rains then take umbrella otherwise not

# syntax: 
#if condition:
#    statement1
#    statement2
#    statement3
#    ...

# in python code must be indent  by the same number of spaces to show that it is inside the if statement   

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
    print("You can drive")

print("This is after first if")

if age < 18:
    print("You are not eligible for voting")
    print("You cannot drive")

print("This is after second if")

if age >= 60:
    print("You are senior citizen")

print("this is after third if")

if age <= 0:
    print("this is not possible")

print("program is still continue till end")
# exit()

# Example 2
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
print("this is after first if")
if number == 0:
    print("Number is zero")
print("this is after second if")
if number < 0:
    print("Negative number")
print("this is after third if")

# Example 3
password = str(input("Enter your password: "))

if len(password) >= 8:
    print("Strong password")
print("after first if")

if len(password) < 8:
    print("Weak password")
print("after second if")

print("program is still continue till end")