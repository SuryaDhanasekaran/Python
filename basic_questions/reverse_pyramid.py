# 1
# 2 1
# 3 2 1
# 4 3 2 1

rows = int(input("Enter Number of Rows:"))
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end="")
    print("")