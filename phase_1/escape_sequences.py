# Here we understand the escape sequences in python

"""
An escape sequence in Python is a combination of characters starting with a backslash (\) 
that represents a special character or action within a string.
"""

# Example 1: Newline (\n)
print("Hello\nWorld")

# Example 2: Tab (\t)
print("Name:\tJohn")

# Example 3: Backslash (\\)
print("This is a backslash: \\")

# Example 4: Single Quote (\')
print('It\'s a beautiful day.')
print("It's a beautiful day.")

# Example 5: Double Quote (\")
print("He said, \"Hello\".")
print("He said, 'Hello'.")

# Example 6: Carriage Return (\r)
print("12345\rABCDE")  # ABCDE will overwrite 12345

# Example 7: Form Feed (\f)
print("Page 1\fPage 2")  # new page

# Example 8: Backspace (\b)
print("Hello\bWorld")  # Deletes 'o'
# exit()
# Example 9: Octal (\ooo) and Hexadecimal (\xhh)
print("\101")  # ASCII for 'A'
print("\x41")  # ASCII for 'A'


# Example 10: String Working
# Difference of "", '', """

print("this is a valid string")
print('this is a valid string')
print("""this is a valid string""")
# exit()
# this is not valid string because it is not enclosed in same quotes
# but if you want to add quotes in string you can use escape sequence
# """ this is valid """
print("this is Uzair's book")
print("""Quaid e Azam was a great leader he said "Unity, Faith and Discipline" is very important to us""")
print('Quaid e Azam was a great leader he said "Unity, Faith and Discipline"')