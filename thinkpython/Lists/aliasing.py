# a refers to a object and you assign b=a, then both variables refer to the same object

a = [1,2,3]
b = a
#IF THE ALIASED OBJECT IS MUTABLE CHANGES MADE WITH ONE ALIAS AFFECT THE OTHER
b[0] = 42
print(a)
print(b is a)