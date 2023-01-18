#Variables and Parameters Are Local

#When you create a variable inside a function,it is local(it only exist inside the function)
#EG:



#stack diagram->(1)(2(3)
def print_twice(any):#The function assigns the argument to the parameter named bruce(3)
    print(any)
    print(any)
    #print_twice(cat) - access cat within print_twice it will give a Name Error # T R A C E  B A C K
def cat_twice(part1, part2):#cattwice(2)
    cat = part1 + part2
    print_twice(cat) #print_twice was called by cat_twice 
line1 = "Bing tiddle "#main(1)
line2 = "tiddle bang."
cat_twice(line1, line2)#cattwice was called by main
#print(cat) #- exception when cat_twice terminates the variable cat is destroyed.
#parameter are also local

#when you create a variable outside a function it belongs to main

#each parameter refers to the same value as it corresponding argument
#part1 = line1
#part2 = line2
#any = cat

#error occured during function call,python prints the name of the function