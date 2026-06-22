# we learn here python operators

"""
we learn here different types of operators
1. arithmetic operators
2. relational operators
3. assignment operators
4. logical operators
5. membership operators
6. identity operators
7. bitwise operators
"""

#  arithmetic operators

a = 10
b = 20
print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division -> answer is always float
print(b/a)
print(a % b)   # modulo -> the remainder of the division
print(a ** b)  # exponentiation it's like (a) ^ (b)
print(a // b)  # floor division -> the greater integer than the quotient of the division (without remainder)
# exit()


# relational operators

print(a > b)   # greater than
print(a < b)   # less than
print(a == b)  # equal to
print(a != b)  # not equal to
print(a >= b)  # greater than or equal to
print(a <= b)  # less than or equal to


# assignment operators

a = b   # this is like => a = b
print(a)

a += b  # this is like => a = a + b
print(a)

a -= b  # this is like => a = a - b
print(a)

a *= b  # this is like => a = a * b
print(a)

a /= b  # this is like => a = a / b
print(a)

a %= b  # this is like => a = a % b
print(a)

a **= b  # this is like => a = a ** b
print(a)

a //= b  # this is like => a = a // b
print(a)
# exit()

# logical operators
c = True
d = False
a = 10
b = 5
print(c and d)   # and -> if both are true then true
print(c or d)    # or -> if either is true then true
print(not c)     # not -> reverse the value

# print(c ^ d)     # xor -> if either is true then true
print("And operator :", (a > b) and (b < a))
print("Or operator :", (a < b) or (b > a))
print("Not operator :", not (a > b))
# exit()

# membership operators
name = "uzair"
print("a" in name)   # in -> if the value is in the string then true
print("w" not in name)   # not in -> if the value is not in the string then true
print("adan" in name)   # in -> if the value is in the string then true
print("was" not in name)   # not in -> if the value is not in the string then true
print("uzair" in name * 2)   # in -> if the value is in the string then true
print("uzair" not in name * 2)   # not in -> if the value is not in the string then true


# identity operators

a = 10
b = 10
name = 'uzair'
print(a is b)   # is -> if the value is in the string then true
print(a is not b)   # not is -> if the value is not in the string then true
print(name is "uzair")
print(name is not "uzair")


# bitwise operators

a = 10
b = 20
print(a & b)   # bitwise and
print(a | b)   # bitwise or
print(a ^ b)   # bitwise xor
print(~a)      # bitwise not it's like taking the two's complement of the number
print(a << b)  # bitwise left shift it's like multiplying the number by 2 to the power of the shift value
print(a >> b)  # bitwise right shift it's like dividing the number by 2 to the power of the shift value