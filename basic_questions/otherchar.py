s = input("Enter a string:")
d = 0
l = 0
o = 0

for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        l+=1
    else:
        o+=1
print("Digits:",d)
print("Letters:",l)
print("Other char",o)