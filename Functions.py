def hello():
    print("hi")
hello()

#functions with arguments
def print_function(word):
    print("Hello"+word)
print_function("pankaj")

#with multiple argumnets
def addition(x,y,z):
    print(x+y+z)
addition(3,5,1)


#Function arguments can be used as variables inside the function definition.
def func(variable):
    variable+=1
    print(variable)
func(6)


#returning functions
def max(x,y):
    if x>y:
        return x
    else:
        return y
print(max(3,6))

#Functions as objects
def multiply(a,b):
    return a*b
a=7
b=2
result=multiply
print(result(a,b))