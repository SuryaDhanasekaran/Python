def testrange(a,b,n):
    if n in range(a,b):
        print("is in range")
    else:
        print("outside the range")

a=int(input("Enter lower limit:"))
b=int(input("Enter upper limit:"))
n = int(input("Enter a number:"))
testrange(a,b,n)