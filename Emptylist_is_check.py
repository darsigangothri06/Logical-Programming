# Checking [] is []
a = []
b = []
print(a is b)  # As list is mutable, id's of a and b are not equal.
print(id(a), id(b))