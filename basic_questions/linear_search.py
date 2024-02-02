list = [1,2,3,4,5,6]

search = int(input("Enter the element to be searched:"))
for i in range(0,len(list)):
    if search==list[i]:
        print(str(search)+" Found at position"+str(i))