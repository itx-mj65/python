marks={
    "john": 85,
    "jane": 90,
    "mike": 75,
    "sarah": 92
}
# print(marks , type(marks))
# print(marks["john"])

# marks["jane"]=88
# print(marks)
# print(marks.keys())
# print(marks.values())
# print(marks.items())

# marks.update({"john":100})
# print(marks)
# marks.get("john")  # returns none if the key you specified does not exist

# del marks["jane"] # delete a key-value pair

# print(marks)

# marks.clear() # delete all key-value pairs

# print(marks)

# pop and pop item

print(marks.pop("john")) # returns the value of the popped item
print(marks)

print(marks.popitem()) # returns a random key-value pair and removes it from the dictionary

print(marks)

# popitem()
# Purpose: Removes and returns the last inserted item (LIFO order in Python 3.7+).

# Arguments: None.

# Returns: A (key, value) tuple of the removed item.

# Errors: Raises KeyError if the dictionary is empty.