print(print("Hello"))
'''
Python evaluates from inner print()
as print() returns None, print(print()) is equivalent to print(None)
'''

print(print(print("hi")))
'''
Evaluated as
print(print(print('hi'))) --- Gives hi
print(print(None)) --- Gives None
print(None) -- Gives None

Output is:
hi
None
None
'''