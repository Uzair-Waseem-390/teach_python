# here we understand the if else if working
# it is used to make decision 
# for example if it rains then take umbrella otherwise not

# if condition1:
    # code
# elif condition2:
    # code
# elif condition3:
    # code
# else:
    # code

# Example 1
num = int(input("Enter a number: "))
if num == 0:
    print("The number is zero")
elif num > 0:
    print("The number is positive")
else:
    print("The number is negative")

print("program is still continue till end")



# Example 2
day = int(input("Enter a day(1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

print("program is still continue till end")


# Example 3
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Grade F")
    


# Example 4
light = input("Enter the light color: ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get Ready")
elif light == "green":
    print("Go")
else:
    print("Invalid color")



