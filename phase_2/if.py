# here we understand the if statement
# it is used to make decision 
# for example if it rains then take umbrella otherwise not

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
