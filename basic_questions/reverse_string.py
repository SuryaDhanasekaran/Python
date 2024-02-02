n = input("Enter a string:")
l = n.split()
l.reverse()
print("Reversed String:",end=" ")
for i in l:
    print(i, end=" ")