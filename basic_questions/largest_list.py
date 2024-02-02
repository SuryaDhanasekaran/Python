def max_num(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print(max_num([1,2,-8,0]))