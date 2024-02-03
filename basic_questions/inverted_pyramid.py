# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2 
# 1

rows = int(input("Enter the number of rows:"))
b = rows
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")
        
        