#this is how we would add two numbers normally
a = 2
b = 3
c = a + b

print(c)  #o/p → 5    we can then print out to the console 'c' or
print(a + b)  #o/p → 5     we can print the expression itself which is 'a+b'

#below is the syntax of a 'function' in python
#we start of by using the 'def' keyword followed by the function name
#in this case 'something' and the followed by paranthesis and a ':'
#python doesn't use '{}' to define the scope of a function it uses a tab (or indent)
#once the next line starts from the very left, it signifies that the previous line was the end of the function
#remember, you don't always have to return something from a function. It's similar to 'void' in other programming languages
#in python you don't have to specify the return type
def something():
    #in the scope of the function
    print('hello')
    
#not in the scope of the function
d = 5

something() #function call. It means that 'hello' would get printed to the console (o/p) → hello

#below is yet another function, but this time it has something called 'parameters'
#parameters are basically arguments that one wants to use in the function
#notice the 'return' statement. That signifies that once the function is done executing it will return a value
#in this case it's returning the sum of the two numbers
def addition(x, y):
    z = x + y
    return z

#since the function is returning something we need to 'catch' it and hence we store it in a variable
#named 'total_score'
total_score = addition(2, 3)  #function call and storing the returned value (2 and 3 will become (x, y) in the function)
print(total_score) #o/p → 5


#to make things simpler, instead of adding another variable 'z' like in the earlier function
#we could just return the sum expression itself
def sum(x, y):
    return x + y


total = sum(2, 3)
print(total)
print(sum(2, 3))
