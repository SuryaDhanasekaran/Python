a = []
b = []
n1 = int(input("Enter a number of elements for list A:"))
for i in range(1,n1+1):
    c = int(input("Enter a element"))
    a.append(c)
n2 = int(input("Enter a number of elements for list B:"))
for i in range(1,n2+1):
    t = int(input("Enter a element"))
    a.append(t)
merge = a + b
merge.sort()
print('sorted list',merge)