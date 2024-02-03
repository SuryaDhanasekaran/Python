def check(a):
    smallest = a[0]
    for i in a:
        if smallest>i:
            smallest = i
    return smallest

print(check([20,30,10,40,50]))