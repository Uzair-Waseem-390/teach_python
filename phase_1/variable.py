# here we learn the variables

print("Hello, World!")

"""
rules for naming variables:
1. Variable names must start with a letter or underscore.
2. Variable names cannot start with a number.
3. Variable names cannot contain spaces.
4. Variable names cannot contain special characters other than underscore.
5. Variable names are case sensitive.
6. Keywords can't be used as variable names. (like if, else, for, while, etc.)


best practices:
7. Variable names should be short, descriptive and meaningful.
8. Variable names should be in lowercase.
9. Variable names should be in snake_case.
10. Variable names should not be too short.
11. Variable names should not be too long.
"""


name = "uzair"
age = 21
height = 5.9
Is_student = True   # this just to let you know variable is case sensitive

# == is not =  (== is for checking the value and = is for assigning the value)
print(type(name))    # the type function is for checking the type of name
print(type(age))
print(type(height))
print(type(Is_student))

print(name == "uzair1")
exit()



print(type(name))
print(type(age))
print(type(height))


print("my name is ", name, "i'm ", age, " years old, and my height is ", height)
# exit()

print("my name is  " + name + " i'm " + str(age) + " years old, and my height is " + str(height))

print(f"my name is {name} i'm {age} years old, and my height is {height}")