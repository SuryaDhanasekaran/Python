li = [1,2,3,4,5,6,7,8,9,10]

for i in li:
    print(i)
    if i == 3:
        li.update(li.index(i),100)