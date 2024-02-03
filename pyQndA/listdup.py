list1 = [10,10,20,30,40,20,30]
list2 = [10,20,30,40,50,60]
#output = [10,10,20,30,40,20,30,50,60]

output=list1
for value in list2:
    if value not in list1:
        output.append(value)
print(output)