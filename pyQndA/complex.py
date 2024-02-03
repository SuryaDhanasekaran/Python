a = [10,20,30]
result = (x for x in a if a.count(x)>0)
a = [40,20,60]
print(list(result))