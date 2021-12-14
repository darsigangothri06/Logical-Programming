# Integer range in python is [-5,256]
# Any integers in between this range have same id's.
a = 23
b = 23
print(a is b)

'''
Python Shell 3.10.0

>>> a = 257
>>> b = 257
>>> print(a is b) # False
    ---> Because in python Shell the allocation of memeory takes line by line when executed
    ---> When a = 257 is executed, the value of a is assigned in one id.
    ---> When b = 257 is executed, python does not know that, already a = 257 is there.
    ---> Separate id for b is allocated.
    ---> Therefore, id's of a and b are different.
    ---> Output is False
    
Eval.py # File name

a = 257
b = 257
print(a is b) # True
---> Here, While executing Eval.py file, the compiler knows that there are two variables pointing to same integer(immutable) type.
---> Therefore, it gives same id's for both a and b.
---> Output is True
'''