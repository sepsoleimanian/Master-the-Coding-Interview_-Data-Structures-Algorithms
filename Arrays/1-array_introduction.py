"""
access -> O(1)
append -> O(1)
insert -> O(n)
delete -> O(n)
"""
strings = ["a", "b", "c", "d"]
print(strings)

strings.append("e") # -> O(1)
# if addeing an iterm at the end of list cause list to be doubled size, then it is  O(N)
print(strings)

strings.pop() # -> O(1)
print(strings)

strings.insert(0,"z") # -> O(n)
print(strings)

strings.insert(2,["x","y","g"]) # -> O(n)
print(strings)

strings[2:2] = ["x", "y", "g"]  # Insert "x", "y", "g" at index 2 -> O(n)
print(strings)

del strings[5] # -> O(n)
print(strings)

print(strings[2]) # -> O(1)


