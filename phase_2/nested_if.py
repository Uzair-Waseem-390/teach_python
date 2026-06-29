# here we understand the nested if structure
# if inside an another if
# it can be used in real life too
# for example if you want to go out side and it is raining then you not able to go out side
# or if you want to go out side and it is not raining then you able to go out side
# here the raining is condition
# if it is raining then you not able to go out side
# else if it is not raining then you able to go out side
# simple words if inside an another if




# Example 1:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
    print("You can drive")
    if age >= 60:
        print("You are senior citizen")
    else:
        print("You are not senior citizen")
else:
    print("You are not eligible for voting")
    print("You cannot drive")

print("program is still continue till end")



# Example 2:
balance = int(input("Enter your balance: "))
amount = int(input("Enter your amount: "))
if balance > 0:
    if amount <= balance:
        print("Withdrawal successful")
        print("Balance after withdrawal: ", balance - amount)
    else:
        print("Insufficient balance")
else:
    print("Invalid balance")



# Example 3:
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance: "))
if marks >= 50:
    if attendance >= 75:
        print("Pass and eligible for certificate.")
    else:
        print("Pass but low attendance.")
else:
    if attendance >= 75:
        print("Failed despite good attendance.")
    else:
        print("Failed and attendance is also low.")




# Example 4:
age = int(input("Enter your age: "))
has_id_card = input("Do you have ID card? (yes/no): ")
if age >= 18:
    print("You are an adult.")

    if has_id_card == "yes":
        print("Entry allowed.")
    else:
        print("ID card required.")

else:
    print("You are under 18.")

    if has_id_card == "yes":
        print("You have an ID card, but age requirement is not met.")
    else:
        print("No ID card and age requirement is not met.")




# Example 5:
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")