#Adding New Functions

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
#def - keyword that indicates function definition
#name of the function - print_lyrics
#rules 1.letters,numbers and underscore are legal 2. first character can't be a number 3.You cant use a keyword as the name of the function
#4.avoid having a variable and a function with the same name.

#empty parentheses - function doesn't take any arguments

#first line - header : rest - body
#header - ends with colon : body - has to be intended(indentation is always four spaces) body can contain any number of statements

#single quote - when apostrophe appears in a string

print(print_lyrics)
print(type(print_lyrics))
print_lyrics()#syntax for calling new function

#defined a function -> use it inside another function

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()
 
