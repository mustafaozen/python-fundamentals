'''
This script exemplifies basic use of numbers and associated methods in python.
For more details: https://docs.python.org/3/tutorial/introduction.html#numbers
'''

# Python can be used as a calculator by just typing the numbers and operators

# Summation:
sum = 1 + 2
print('The sum is: ', sum, '\n')

# Similarly:
subs = 2 - 1
mult = 3*2
div = 6/2
print('The subs is: ', subs, '\n')
print('The mult is: ', mult, '\n')
print('The div is: ', div, '\n')

# Power of a number:
p = 2 ** 4
print('2 to the power 4 is: ', p, '\n')

# mod of a number:
mod2 = 11 % 2 # returns reminder of 11/2
print('11 mod 2 is: ', mod2, '\n')

## Some useful built-in methods: ##

# abs(num): returns the absolute value of num
absVal = abs(-10)
print('Absolute value of -10 is: ', absVal, '\n')

# pow(num,p): returns pth power of num
p = pow(5,2)
print('5^2 is: ', p, '\n')

# max(num1, num2): returns maximum of num1 and num2
maxNum = max(7,8)
print('The maximum of 7 and 8 is: ', maxNum, '\n')

# min(num1, num2): returns minimum of num1 and num2
minNum = min(7,8)
print('The minimum of 7 and 8 is: ', minNum, '\n')

# round(num): rounds num into closest integer
rounded = round(3.51)
print('The rounded number is: ', rounded, '\n')

# str(num): Casts the number into a string
strNum = str(3.24)
print('This is the string of ' + strNum, '\n')

## Some other functions can be reached through Math library of python. Therefore, import the following library:
from math import *

# floor(num): rounds down the number
rounded = floor(3.51)
print('The floor of 3.51 is: ', rounded, '\n')

# ceil(num): rounds up the number
rounded = ceil(3.51)
print('The ceil of 3.51 is: ', rounded, '\n')

# sqrt(num): returns square root of the number
sqrtNum = sqrt(9)
print('Square root of 9 is: ', sqrtNum, '\n')