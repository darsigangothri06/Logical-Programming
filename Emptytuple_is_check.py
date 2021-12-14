# Checking () is ()
a = ()
b = ()
print(a is b)  # As tuple is immutable, id's of a and b are equal.
print(id(a), id(b))