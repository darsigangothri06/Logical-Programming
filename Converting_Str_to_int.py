# Converting a string to integer
a = "10"
print(int(a)) # 10 --- int() can convert only integral strings to integers.

b = "120.3"
print(int(b)) # ValueError, int() cannot convert a float string.