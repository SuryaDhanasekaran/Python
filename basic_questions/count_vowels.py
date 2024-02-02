s = input("Enter a string:")
c = 0
for i in s:
    if i in "aeiouAEIOU":
        c += 1
print("The number of vowels in",s,"is",c)