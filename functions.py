def avg():  # this is called function definition
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    avg=(a+b+c)/3
    print("The average of the numbers is: ",avg)
    return avg  # this is called function return

function_return= avg()  # this is called function call

print("The returned value from the function is: ", function_return)  # this is called function call

# arguments and parameters are same in function definition and function call
# but in function definition they are called parameters and in function call they are called argument
def add(x,y):
    return x+y

print(add(5,6))  # function call with arguments

# builtin functionss
print(abs(-5))  # absolute value

print(max(3,5,6))  # maximum value

print(min(3,5,6))  # minimum value

print(pow(2,3))  # power

print(round(3.75))  # round off value

print(sum([1,2,3,4,5]))  # sum of all numbers

print(len([1,2,3,4,5]))  # length of list

print(sum([1,2,3,4,5])/len([1,2,3,4,5]))  # average of numbers

print(sorted([1,3,8,4,5]))  # sorted list

print(sorted([1,3,8,4,5], reverse=True))  # sorted list in descending order

# default parameter values

def greet(name="User"):
    return "Hello, " + name

print(greet("jamshiad" ))  # default parameter value

# recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    print(factorial(5))  # factorial of 5

# another example of recursive function 
# a function that calls itself in its own definition
# ek function jo apni khud ki definition mein apni khud ko call karta hai
# daily life example: a hypothetical function to calculate the factorial of a number

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
    print(factorial_recursive(5))  # factorial of 5
    # in this case, the function calls itself in its own definition, thus making it a recursive function

fac = factorial_recursive(5)

print("Factorial of 5 using recursive function is:", fac)
