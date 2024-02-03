# input:
# odd_num_list, even_num_list
# output:
# oddevenoddeven ->list

odd_num_list = [1,3,5,7,9]
even_num_list = [2,4,6,8,10]

for num1,num2 in zip(odd_num_list,even_num_list):
    print(num1)
    print(num2)