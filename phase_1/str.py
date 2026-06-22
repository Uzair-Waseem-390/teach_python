# here we understand the string behavior
"""
1.string is immutable means we can't change the string
2.string are sequence of characters
3.slicing is used to get the substring
4.concatenation is used to join strings
5.repetition is used to repeat strings
6.membership operators are used to check if a string is in another string
7.relational operators are used to compare strings
"""
# example
name = "uzair waseem"


print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

print(len(name))

# exit()
print("uzair" != "uzair1")



# str slicing
name = "uzair waseem"
print(name[3::3])
print(name[1:3])         # start(inclusive):stop(exclusive)
print(name[1:10:2])       # start:stop:step
print(name[-1])          # last element
print(name[-2])          # second last element
print(name[::-1])        # reverse (step is -1)
print(name[::2])         # step
print(name[1::2])        # start:stop:step
print(name[:3:2])        # start:stop:step
print(name[::-2])        # start:stop:step (reverse)
print(name[-1:-4:-2])    # start:stop:step (reverse)
print(name[1:4:-2])      # start:stop:step (reverse)
print(name[-1:-4:2])     # start:stop:step (reverse)
print(name[-1:-4:2])     # start:stop:step (reverse)

exit()
# str concatenation & repetition

name = "uzair "

print(name + " waseem")
# print("uzair" + "23")

print(name * 5)

print(len(name * 2))
print(name * 2 + " waseem")


# str membership operators
name = "uzair waseem"

print("a" in name)
print("w" not in name)
print("adan" in name)
print("was" not in name)
print("uzair" in name * 2)
print("uzair" not in name * 2)



# str relational operators
name = "uzair waseem"
print(name > "uzair")
print(name < "uzair")
print(name == "uzair")
print(name != "uzair")
print(name >= "uzair")
print(name <= "uzair")
exit()

# str methods
name = "   uzair waseem   "

print(name.upper())       # convert to uppercase
print(name.lower())       # convert to lowercase
print(name.title())       # convert to title case
print(name.capitalize())    # convert to capitalize case
print(name.swapcase())    # swap case
print(name.strip())       # remove whitespace from both sides
print(name.lstrip())      # remove whitespace from left side
print(name.rstrip())      # remove whitespace from right side
print(name.replace("uzair", "waseem"))     # replace substring
print(name.find("i"))     # find substring
print(name.index("i"))    # find substring
print(name.count("u"))    # count substring
print(name.startswith("u"))   # check if string starts with substring
print(name.endswith("r"))   # check if string ends with substring
print(name.split())       # split string
print(name.join(name))    # join strings
print(name.partition("uzair"))    # partition
print(name.rpartition("uzair"))   # partition from right
print(name.split(" "))    # spl it string
print(name.split(" ", 1))  # split string