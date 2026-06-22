# here we learn input statement


"""
to get input from the user we use input() function
input() function always return string
input() function can take one argument which is the prompt string to be displayed to the user
"""
name = input("enter your name : ")
print("Welcome ",name, "to our website")

age = input("enter your age : ")
height = input("enter your height : ")

print("your name is ", name)
print("your age is ", age)
print("your height is ", height)

# by default input is string

print("type of name is :", type(name))
print("type of age is :", type(age))
print("type of height is :", type(height))

# typecasting

name = str(name)
age = int(age)
height = float(height)

print("type of name is :", type(name), "name is", name)
print("type of age is :", type(age), "age is", age)
print("type of height is :", type(height), "height is", height)
exit()
# but we can also provide the type of input

name = input("enter your name : ")
age = int(input("enter your age : "))
height = float(input("enter your height : "))

print("your name is ", name, "type of name is ", type(name))
print("your age is ", age, "type of age is ", type(age))
print("your height is ", height, "type of height is ", type(height))
exit()