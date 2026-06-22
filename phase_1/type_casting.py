# here we understand the type casting

"""
what is type casting?
-> when we convert one data type to another data type is called type casting
-> type casting is also known as type conversion
-> there are two types of type casting:
    1. explicit type casting
    2. implicit type casting

when is explicit type casting used?
-> when we want to convert one data type to another data type manually
-> when we want to convert one data type to another data type forcefully
-> when we want to convert one data type to another data type
"""
# examples of explicit type casting

name = "uzair"
age = 21
height = 5.9
truth = True

print("type of name is :", type(name))
print("type of age is :", type(age))
print("type of height is :", type(height))
print("type of truth is :", type(truth))


# here all the variables are of different data types
# now we convert them to same data type

name = name
age = str(age)
height = str(height)
truth = str(truth)

# now all the variables are of same data type

print("type of name after typecasting is :", type(name))
print("type of age after typecasting is :", type(age))
print("type of height after typecasting is :", type(height))
print("type of truth after typecasting is :", type(truth))


# examples of implicit type casting

age = 21
height = 5.9
print(type(age))
print(type(height))

ans = age + height
print("type of ans is :", type(ans))
print(ans)


