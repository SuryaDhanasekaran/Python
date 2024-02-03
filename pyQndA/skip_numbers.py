#Input = [1,2,3,4,5,6,7,8,9,10]
#Output = [1,2,3,4,6,7,8,10]

input = [1,2,3,4,5,6,7,8,9,10]
output = []
for i in input:
    if i==5 or i==9:
        continue
    output.append(i)
print(output)
    