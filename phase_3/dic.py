# Here we'll cover the python dictionary in detail
# dictionary is a collection type in python which is used to store data in KEY : VALUE pairs
# Example: d = {"name": "Ali", "age": 20}
# dictionary is mutable data type
# dictionary is ordered data type (insertion order is preserved, since Python 3.7+)
# dictionary keys do NOT allow duplicates, but values CAN be duplicated
# dictionary does NOT support indexing by position, you access items by KEY
# dictionary keys must be immutable/hashable (str, int, tuple, etc.), values can be anything


# How to create a dictionary
dict1 = {"name": "Ali", "age": 20, "city": "Lahore"}    # dictionary of key:value pairs
dict2 = dict()                                          # Empty dictionary using constructor
dict3 = {}                                              # Empty dictionary using {}
dict4 = {1: "one", 2: "two", 3: "three"}                # dictionary with integer keys
dict5 = {"student": {"name": "Sara", "age": 22}}         # Nested dictionary
dict6 = dict(name="Uzair", age=25, city="Karachi")       # creating a dictionary using dict()


# How to access dictionary items
dict1 = {"name": "Ali", "age": 20, "city": "Lahore"}
print(dict1["name"])          # Access value by key
print(dict1["age"])
print(dict1.get("city"))      # get() is the SAFER way to access a value
print(dict1.get("country"))   # returns None instead of raising an error if key doesn't exist
print(dict1.get("country", "Not Found"))   # get() can also take a default value

print(dict1.keys())      # Returns all the keys
print(dict1.values())    # Returns all the values
print(dict1.items())     # Returns all key:value pairs as tuples


# Change dictionary items
dict1 = {"name": "Ali", "age": 20, "city": "Lahore"}
dict1["age"] = 21              # change the value of an existing key
print(dict1)

dict1.update({"age": 22, "country": "Pakistan"})   # update() can change/add multiple keys at once
print(dict1)


# Add dictionary items
dict1 = {"name": "Ali"}
dict1["age"] = 20        # adding a new key:value pair (same syntax as changing an item)
print(dict1)

dict1.setdefault("city", "Lahore")    # setdefault() adds the key ONLY IF it doesn't already exist
print(dict1)
dict1.setdefault("name", "Fatima")     # since "name" already exists, its value stays unchanged
print(dict1)


# Remove dictionary items
dict1 = {"name": "Ali", "age": 20, "city": "Lahore", "country": "Pakistan"}

a = dict1.pop("age")        # pop() removes the key and RETURNS its value
print(a)
print(dict1)

a = dict1.popitem()          # popitem() removes and returns the LAST inserted key:value pair
print(a)
print(dict1)

del dict1["city"]              # del removes a key:value pair by key
print(dict1)

dict1.clear()                    # clear() empties the dictionary
print(dict1)   # {}


# Looping through a dictionary
dict1 = {"name": "Ali", "age": 20, "city": "Lahore"}

for key in dict1:                 # looping directly gives you the KEYS
    print(key)

for key in dict1.keys():          # explicit way to loop through keys
    print(key)

for value in dict1.values():       # looping through values
    print(value)

for key, value in dict1.items():    # looping through key:value pairs together
    print(key, ":", value)


# Copying a dictionary
dict1 = {"name": "Ali", "age": 20}
dict2 = dict1.copy()      # copy() creates a shallow copy
dict2["age"] = 99
print(dict1)   # original dictionary is unaffected
print(dict2)


# Merging dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = d1 | d2            # merge operator (Python 3.9+), values from d2 win on duplicate keys
print(merged)   # {'a': 1, 'b': 3, 'c': 4}

d1 |= d2                     # update d1 in place with items from d2
print(d1)


# Searching in a dictionary
d = {"name": "Ali", "age": 20, "city": "Lahore"}

if "name" in d:            # 'in' checks the KEYS by default, not the values
    print("Present")
else:
    print("Not Present")

if "country" not in d:
    print("Not Present")
else:
    print("Present")

if "Ali" in d.values():     # to search for a VALUE, check inside .values()
    print("Value Present")