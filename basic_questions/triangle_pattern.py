rows = int(input("Enter a number of rows: "))

for row in range(rows+1):
    for column in range(row):
        print(row, end="")
    print(" ")