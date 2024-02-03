input = [1,2,3,4,5,6,7,8,9,10]
# output = [1,2,3,4,5,10,9,8,7,6]

mid = len(input)//2
output = []

for i in range(1,len(input)):
    if i < mid + 1:
        output.append(i)
        continue
    else:
        for j in input[::-1]:
            if j != 5:
                output.append(j)
                continue
            break
    break
print(output)