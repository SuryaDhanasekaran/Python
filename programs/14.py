#Parameters and Arguments

#some functions require arguments.eg.math.sin you pass number as argument.some functions take more than one argument
#math.pow takes two,the base and the exponent

#inside function the arguments are assigned to variables called parameters.
import math
def print_twice(any):#The function assigns the argument to the parameter named brucr
    print(any)
    print(any)
    print("Hello")
print_twice('Spam')
    #when function is called it prints the value of the parameter twice
print_twice(42)
print_twice(math.pi)#any kind of expression can be given as an argument for print_twice
print_twice('Spam '*4)
print_twice(math.cos(math.pi))
#you can also use an variable as an argument
surya = 'Eric, the half a bee.'
print_twice(surya)