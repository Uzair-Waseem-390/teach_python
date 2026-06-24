# here we understand the if else working
# if condition is false then else block is execute
# if condition is true then if block is execute

# if condition:
    # runs if condition is True
# else:
    # runs if condition is False


# Example 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
    print("You can drive")
else:
    print("You are not eligible for voting")
    print("You cannot drive")

print("This is after if else")

if age >= 60:
    print("You are senior citizen")
else:
    print("You are not senior citizen")

if age <= 0:
    print("this is not possible")


print("program is still continue till end")



# Example 2
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
    print("this is even block")
else:
    print("The number is odd")
    print("this is odd block")

print("program is still continue till end")



# Example 3
marks = int(input("Enter your marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")



# Example 4
username = input("Enter your username: ")
if username.lower() == "admin":
    print("Access granted")
else:
    print("Access denied")




# Example 5
balance = int(input("Enter your balance: "))
if balance >= 1000:
    print("Withdrawal allowed")
else:
    print("Insufficient balance")




# Example 6
temperature = int(input("Enter your temperature: "))
if temperature > 30:
    print("It is hot.")
else:
    print("It is not hot.")