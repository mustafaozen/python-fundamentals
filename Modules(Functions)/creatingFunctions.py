'''
This script exemplifies how to create functions (modules) and how to use them in python. It also exemplifies usage of lambda expression.
For more details:
https://docs.python.org/3/tutorial/modules.html
'''

# Thanks to functions (modules), we can prevent repeating the same code segments and make our codes more optimized and organized.

# The general structure of functions is as follows:
def myFunction(var):
    # type your code segment
    print(var)

# Lets write a function that calculates Pth power of number

def powerOfNum(num, pow):
    result = num ** pow
    return result

# Now, whenever we need to calculate power of a number, we can use this function!

pow1 = powerOfNum(3,4)
pow2 = powerOfNum(2,8)

print('3 to the power 4 is: ', pow1, '\n')
print('2 to the power 8 is: ', pow2, '\n')

## Lambda Expressions ##

# Lambda expressions are defined as anonymous functions. This is another way of defining the functions.

fun = lambda n,p: n ** p
pow3 = fun(7,2)
print('7 to the power 2 is: ', pow3, '\n')
