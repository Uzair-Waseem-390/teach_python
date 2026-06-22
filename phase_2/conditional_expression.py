# here we understand the conditional expression 
# it is a way to write if-else in a single line


# Syntax
# value_if_true if condition else value_if_false


# Example 1: Simple conditional expression

num = int(input("Enter a number: "))
result = "Positive" if num > 0 else "Not Positive"
print(result)


# Example 2: Check if a number is even or odd

num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(result)


# Example 3: Check if a person is eligible for voting

age = int(input("Enter your age: "))
result = "Eligible" if age >= 18 else "Not Eligible"
print(result)


# Example 4: Check if a number is greater than 10

num = int(input("Enter a number: "))
result = "Greater than 10" if num > 10 else "Less than 10"
print(result)


# Example 5: Check if a number is positive, negative or zero

num = int(input("Enter a number: "))
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)



# Example 6: Check if a number is within range

num = int(input("Enter a number: "))
result = "In range" if 0 <= num <= 100 else "Out of range"
print(result)


# Example 7: Check if a number is divisible by 5

num = int(input("Enter a number: "))
result = "Divisible by 5" if num % 5 == 0 else "Not divisible by 5"
print(result)



# Example 8: Check if a number is a perfect square

num = int(input("Enter a number: "))
result = "Perfect square" if num ** 0.5 == int(num ** 0.5) else "Not a perfect square"
print(result)


# Example 9: Check if a number is prime

num = int(input("Enter a number: "))
result = "Prime" if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) else "Not a prime"
print(result)


# Example 10: Check if a number is a power of 2

num = int(input("Enter a number: "))
result = "Power of 2" if num > 0 and (num & (num - 1)) == 0 else "Not a power of 2"
print(result)