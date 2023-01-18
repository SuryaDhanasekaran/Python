# Total wholesale book cost calculator
cover_price = 24.95

number_of_books = int(input("How many books do you want to order at wholesale? "))

def ship_cost (number_of_books):
    if number_of_books == 1:
        return (number_of_books * 3) # Cost of shipping one book is $3
    else:
        return (3 + (number_of_books - 1) * 0.75) # Each additional copy of the book is $0.75 to ship

def discounted_price(number_of_books):
    return(cover_price - (cover_price * .4)) # There is a 40% discount on wholesale book sales

def wholesale_cost(number_of_books):
    return ((discounted_price(number_of_books) * number_of_books) + ship_cost(number_of_books))

print("The cost of buying and shipping", number_of_books, "books is $",round(wholesale_cost(number_of_books), 2))
